import unittest

from protein_translation import of_codon, of_rna

# Tests adapted from problem-specifications/canonical-data.json @ v1.0.0

class ProteinTranslationTests(unittest.TestCase):

    def test_AUG_translates_to_methionine(self):
        self.assertEqual('Methionine', of_codon('AUG'))

    def test_identifies_Phenylalanine_codons(self):
        for codon in ['UUU', 'UUC']:
            self.assertEqual('Phenylalanine', of_codon(codon))

    def test_identifies_Leucine_codons(self):
        for codon in ['UUA', 'UUG']:
            self.assertEqual('Leucine', of_codon(codon))

    def test_identifies_Serine_codons(self):
        for codon in ['UCU', 'UCC', 'UCA', 'UCG']:
            self.assertEqual('Serine', of_codon(codon))

    def test_identifies_Tyrosine_codons(self):
        for codon in ['UAU', 'UAC']:
            self.assertEqual('Tyrosine', of_codon(codon))

    def test_identifies_Cysteine_codons(self):
        for codon in ['UGU', 'UGC']:
            self.assertEqual('Cysteine', of_codon(codon))

    def test_identifies_Tryptophan_codons(self):
        self.assertEqual('Tryptophan', of_codon('UGG'))

    def test_identifies_stop_codons(self):
        for codon in ['UAA', 'UAG', 'UGA']:
            self.assertEqual('STOP', of_codon(codon))

    def test_translates_rna_strand_into_correct_protein_list(self):
        strand = 'AUGUUUUGG'
        expected = ['Methionine', 'Phenylalanine', 'Tryptophan']
        self.assertEqual(expected, of_rna(strand))

    def test_stops_translation_if_stop_codon_at_beginning_of_sequence(self):
        strand = 'UAGUGG'
        expected = []
        self.assertEqual(expected, of_rna(strand))

    def test_stops_translation_if_stop_codon_at_end_of_two_codon_sequence(self):
        strand = 'UGGUAG'
        expected = ['Tryptophan']
        self.assertEqual(expected, of_rna(strand))

    def test_stops_translation_if_stop_codon_at_end_of_three_codon_sequence(self):
        strand = 'AUGUUUUAA'
        expected = ['Methionine', 'Phenylalanine']
        self.assertEqual(expected, of_rna(strand))

    def test_stops_translation_if_stop_codon_in_middle_of_six_codon_sequence(self):
        strand = 'UGGUGUUAUUAAUGGUUU'
        expected = ['Tryptophan','Cysteine','Tyrosine']
        self.assertEqual(expected, of_rna(strand))


if __name__ == '__main__':
    unittest.main()
