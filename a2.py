def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return 0 if len(dna) == 0 else dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGC')
    False

    """

    valid_nucleotides = "ATCG"
    invalid_counter = 0

    for i in dna:
        if not i in valid_nucleotides:
            invalid_counter = invalid_counter + 1

    return invalid_counter == 0


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str


    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCGGC', 'GT', 0)
    'GTATCGGC'
    >>> insert_sequence('ATCGGC', 'GT', 5)
    'GTATCGGC'

    """

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """ (str) -> str

    Returns the nucleotide's complement.

    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'

    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return "Error"


def get_complementary_sequence(dna):
    """ (str) -> str

    Returns the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'

    """

    complementary_sequence = ''

    for i in dna:
        complementary_sequence = complementary_sequence + get_complement(i)

    return complementary_sequence