class bib:
   def __init__(self, data):
       self.data = data
   def __iter__(self):
       for item in self.data:
           yield item
bobik = bib(['Oleg','Sasha','German','Nikita','Bob'])
for item in bobik:
   print(item)