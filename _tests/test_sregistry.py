#!/usr/env python

import unittest
from subprocess import (
    Popen,
    PIPE,
    STDOUT
)
from glob import glob
import requests
import os
import yaml
 

class TestSRegistry(unittest.TestCase):
 
    def setUp(self):
        self.existing = glob('_registries/*')
        process = Popen(['git','diff-tree','--no-commit-id','--name-only','-r','HEAD'], stderr=PIPE, stdout=PIPE)
        added,error = process.communicate()
        added = [x for x in added.decode('utf-8').split('\n') if x]
        self.added = [x for x in added if x.startswith('_registries')] 
        self.lookup = self.load_registries()

    def print_registry_name(self,registry):
        print('Testing Registry %s %s' %os.path.basename(registry).strip('.md'))            

    def load_registries():
        '''read metadata from newly added registries'''
        metadata = dict()
        for registry in self.added:
            uid = os.path.basename(registry).strip('.md')
            uid = re.sub('-registry$','', uid)
            with open(registry, "r") as stream:
                docs = yaml.load_all(stream)
                for doc in docs:
                    if isinstance(doc,dict):
                        for k,v in doc.items():
                            print('%s: %s' %(k,v))
                            metadata[k] = v
            metadata['uid'] = uid
            self.lookup[registry] = metadata


    def test_endpoints(self):
        ''' test registry endpoints serve expected metadata '''
        print("Testing registry endpoints.")

        for registry in self.added:
            self.print_registry_name(registry)
            metadata = self.lookup[registry]
            response = requests.get(metadata['base'])
            self.assertEqual(response.status_code,200)

    def test_filenames(self):
        for registry in self.added:
            self.print_registry_name(registry)
            self.assertTrue(registry.endswith('md'))
            

    def test_markdown_metadata(self):
        '''ensure that fields are present in markdown file'''

        print("Checking markdown fields...")

        for registry in self.added:
            self.print_registry_name(registry)
            fields = ['layout', 'base', 'date', 'author', 'categories',
                      'img','thumb','tagged','institution', 'title']
            metadata = self.lookup[registry]
            for field in fields:
                self.assertTrue(field in metadata)
                self.assertTrue(metadata[field] not in ['', None])


    def test_served_metadata(self):
        '''metadata served by a registry should match the 
           metadata provided in the markdown file'''
 
        print("Matching registry metadata.")

        for registry in self.added:
            self.print_registry_name(registry)
            metadata = self.lookup[registry]
            idcard = '%s/api/registry/identity' %metadata['base'] 
            response = requests.get(idcard)
            self.assertEqual(response.status_code,200)
            card = response.json()

            fields = ['id', 'name', 'url']
            for field in fields:
                self.assertTrue(field in card)
            self.assertEqual(metadata['uid'],card['id'])
            self.assertEqual(metadata['base'],card['url'])
            self.assertEqual(metadata['title'],card['name'])
            self.assertEqual(metadata['layout'],'registry')



if __name__ == '__main__':
    unittest.main()
