def dna_verification(dna:str) -> bool:
    """
    Takes DNA sequence as input and check if all characters are nucleotides
    :param dna: A DNA sequence as string
    :return: True or False
    """
    return set(dna).issubset({'A', 'T', 'G', 'C'})


def dna_to_rna_transcribe(dna:str) -> str:
    """
    Takes DNA sequence as input and replace T-nucleotides to U-nucleotides
    :param dna: A DNA sequence as string
    :return: A RNA sequence as string
    """
    rna = dna.replace('T', 'U')
    return rna


def main():
    sequence = input('Enter a DNA sequence: ')
    dna = sequence.upper()
    if dna_verification(dna):
        print(f'DNA sequence : {dna}')
        print(f'RNA sequence : {dna_to_rna_transcribe(dna)}')
    else:
        print('This sequence is not a DNA sequence')


main()