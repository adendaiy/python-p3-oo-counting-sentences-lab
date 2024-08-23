#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value  # Default value is an empty string
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")


    def is_sentence(self):
        return self.value.endswith('.')  
    def is_question(self):
        return self.value.endswith("?") 
    def is_exclamation(self):
        return self.value.endswith("!")    
    
    def count_sentences(self):
        # Replace multiple punctuation marks with a single period
        cleaned_value = self.value.replace('!', '.').replace('?', '.')
        # Split the string by period
        sentences = cleaned_value.split('.')
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip() != '']
        return len(non_empty_sentences)
