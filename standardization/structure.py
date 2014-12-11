from Bio import SeqIO

# Helix, beta strand and turn score

structures= {
    'score' : {'SequenceId' : 0 , 'helix' : 0 , 'beta strand' : 0 , 'turn' : 0}
    }
    
stats = {
    'seq': {'presence': 0, 'length': 0, 'type': None},
    'id': {'presence': 0, 'length': 0, 'type': None},
    'name': {'presence': 0, 'length': 0, 'type': None},
    'description': {'presence': 0, 'length': 0, 'type': None},
    'dbxrefs': {'presence': 0, 'length': 0, 'type': None},
    'features': {'presence': 0, 'length': 0, 'type': None},
    'annotations': {'presence': 0, 'length': 0, 'type': None},
    'letter_annotations': {'presence': 0, 'length': 0, 'type': None},
    }

sequences = SeqIO.parse("proteinSample.xml", 'uniprot-xml')
for s in sequences:
    for attr in stats:
        if attr =='id':
            structures['score']['SequenceId'] = getattr(s, attr)
        if attr == 'features' :
            print getattr(s,attr)
            while 'helix' in getattr(s,attr) :
                structures['score']['helix'] +=1
    print structures,"\n\n"
    
    


