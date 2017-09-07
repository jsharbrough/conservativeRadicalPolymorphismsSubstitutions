# -*- coding: utf-8 -*-
import sys
def polSub(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    asexList = []
    logfile = open(fasta[0:-5] + 'log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
            if '*' in seq:
                sexList.append(seq)
            else:
                asexList.append(seq)
        else:
            outList.append(seq)
    refSeq = seqDict[sexList[0]]
    outSeq = seqDict[outList[0]]
    outCodons = codonDict[outList[0]]
    popInvariantSites = []
    popPolymorphicSites = []
    logfile.write('Total polymorphisms\n')
    sys.stdout.write('Total Polymorphisms\nGene\tSite\tCodon\tAlleles\tAAs\tPol/Div\tMutation Type\t1\t2\t3\t4\t5\t6\t7\tC/R Index\t2*pq\n')
    i = 0
    sum2PQ_S = 0
    sum2PQ_N = 0
    sum2PQ_C1 = 0
    sum2PQ_C2 = 0
    sum2PQ_C3 = 0
    sum2PQ_C4 = 0
    sum2PQ_C5 = 0
    sum2PQ_C6 = 0
    sum2PQ_C7 = 0
    sum2PQ_R1 = 0
    sum2PQ_R2 = 0
    sum2PQ_R3 = 0
    sum2PQ_R4 = 0
    sum2PQ_R5 = 0
    sum2PQ_R6 = 0
    sum2PQ_R7 = 0
    sum2PQ_meanC = 0
    sum2PQ_meanR = 0
    synS = 0
    nsynS = 0
    con1S = 0
    con2S = 0
    con3S = 0
    con4S = 0
    con5S = 0
    con6S = 0
    con7S = 0
    meanConS = 0
    rad1S = 0
    rad2S = 0
    rad3S = 0
    rad4S = 0
    rad5S = 0
    rad6S = 0
    rad7S = 0
    meanRadS = 0
    N = len(popList)
    sexN = len(sexList)
    asexN = len(asexList)
    while i < len(codonDict[seqList[0]]):
        outCodon = outCodons[i]
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i*3 >= start and i*3 <= stop:
                gene = positionDict[locus]
        currAlleleDict = {}
        currAlleleList = []
        currAADict = {}
        for seq in popList:
            currCodons = codonDict[seq]
            currCodon = currCodons[i]
            if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                currAlleleDict[currCodon] = 1
                currAlleleList.append(currCodon)
            elif 'N' not in currCodon and '-' not in currCodon:
                currValue = currAlleleDict[currCodon]
                currValue += 1
                currAlleleDict[currCodon] = currValue
        if len(currAlleleDict) < 2:
            popInvariantSites.append(i*3)
            popInvariantSites.append((i*3) + 1)
            popInvariantSites.append((i*3) + 2)
        else:
            totalIndividuals = 0
            site1 = []
            site2 = []
            site3 = []
            for codon in currAlleleList:
                totalIndividuals += currAlleleDict[codon]
                if codon[0] not in site1:
                    site1.append(codon[0])
                if codon[1] not in site2:
                    site2.append(codon[1])
                if codon[2] not in site3:
                    site3.append(codon[2])
            currFreqDict = {}
            totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
            variableSites = []
            if len(site1) == 1:
                popInvariantSites.append(i*3)
            else:
                popPolymorphicSites.append(i*3)
                variableSites.append(i*3)
            if len(site2) == 1:
                popInvariantSites.append((i*3) + 1)
            else:
                popPolymorphicSites.append((i*3) + 1)
                variableSites.append((i*3) + 1)
            if len(site3) == 1:
                popInvariantSites.append((i*3) + 2)
            else:
                popPolymorphicSites.append((i*3) + 2)
                variableSites.append((i*3) + 1)
            aaList = []
            twoPQ = 2
            for codon in currAlleleDict:
                freq = float(currAlleleDict[codon])/totalIndividuals
                currFreqDict[codon] = freq
                if i == 0 and codon in startCodons:
                    aa = 'M'
                else:
                    aa = geneticCode[codon]
                currAADict[codon] = aa
                if aa not in aaList:
                    aaList.append(aa)
            if totalChanges == 1:
                for codon in currAlleleDict:
                    freq = currFreqDict[codon]
                    twoPQ *= freq
                if len(aaList) == 1:
                    synS += 1
                    sum2PQ_S += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                else:
                    nsynS += 1
                    sum2PQ_N += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN')
                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    if mutType[0] == 0:
                        con1S += 1
                        sum2PQ_C1 += twoPQ
                    else:
                        rad1S += 1
                        sum2PQ_R1 += twoPQ
                    if mutType[1] == 0:
                        con2S += 1
                        sum2PQ_C2 += twoPQ
                    else:
                        rad2S += 1
                        sum2PQ_R2 += twoPQ
                    if mutType[2] == 0:
                        con3S += 1
                        sum2PQ_C3 += twoPQ
                    else:
                        rad3S += 1
                        sum2PQ_R3 += twoPQ
                    if mutType[3] == 0:
                        con4S += 1
                        sum2PQ_C4 += twoPQ
                    else:
                        rad4S += 1
                        sum2PQ_R4 += twoPQ
                    if mutType[4] == 0:
                        con5S += 1
                        sum2PQ_C5 += twoPQ
                    else:
                        rad5S += 1
                        sum2PQ_R5 += twoPQ
                    if mutType[5] == 0:
                        con6S += 1
                        sum2PQ_C6 += twoPQ
                    else:
                        rad6S += 1
                        sum2PQ_R6 += twoPQ
                    if mutType[6] == 0:
                        con7S += 1
                        sum2PQ_C7 += twoPQ
                    else:
                        rad7S += 1
                        sum2PQ_R7 += twoPQ
                    if mutType[7] <= 0.5:
                        meanConS += 1
                        sum2PQ_meanC += twoPQ
                    else:
                        meanRadS += 1
                        sum2PQ_meanR += twoPQ
                    for item in mutType[0:-1]:
                        if item == 0:
                            sys.stdout.write('\tC')
                        else:
                            sys.stdout.write('\tR')
                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ) + '\n')
            elif totalChanges == 2:
                if len(currAlleleDict) == 3:
                    ab = 0
                    ac = 0
                    bc = 0
                    codonA = currAlleleList[0]
                    codonB = currAlleleList[1]
                    codonC = currAlleleList[2]
                    
                    if codonA[0] != codonB[0]:
                        ab += 1
                    if codonA[1] != codonB[1]:
                        ab += 1
                    if codonA[2] != codonB[2]:
                        ab += 1
                    if codonA[0] != codonC[0]:
                        ac += 1
                    if codonA[1] != codonC[1]:
                        ac += 1
                    if codonA[2] != codonC[2]:
                        ac += 1
                    if codonC[0] != codonB[0]:
                        bc += 1
                    if codonC[1] != codonB[1]:
                        bc += 1
                    if codonC[2] != codonB[2]:
                        bc += 1
                    if ab == ac and ac == bc:
                        if 'N' not in outCodon and '-' not in outCodon:
                            if outCodon == codonA:
                                aaList1 = [currAADict[codonA],currAADict[codonB]]
                                aaList2 = [currAADict[codonA],currAADict[codonC]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sum2PQ_S += twoPQ1
                                        sum2PQ_N += twoPQ2
                                        synS += 1
                                        nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            con1S += 1
                                            sum2PQ_C1 += twoPQ2
                                        else:
                                            rad1S += 1
                                            sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            con2S += 1
                                            sum2PQ_C2 += twoPQ2
                                        else:
                                            rad2S += 1
                                            sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            con3S += 1
                                            sum2PQ_C3 += twoPQ2
                                        else:
                                            rad3S += 1
                                            sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            con4S += 1
                                            sum2PQ_C4 += twoPQ2
                                        else:
                                            rad4S += 1
                                            sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            con5S += 1
                                            sum2PQ_C5 += twoPQ2
                                        else:
                                            rad5S += 1
                                            sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            con6S += 1
                                            sum2PQ_C6 += twoPQ2
                                        else:
                                            rad6S += 1
                                            sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            con7S += 1
                                            sum2PQ_C7 += twoPQ2
                                        else:
                                            rad7S += 1
                                            sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            meanConS += 1
                                            sum2PQ_meanC += twoPQ2
                                        else:
                                            meanRadS += 1
                                            sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    nsynS += 1
                                    synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sum2PQ_S += twoPQ2
                                    sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ2
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ2
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ2
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ2
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ2
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ2
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ2
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ2
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n') 
                            elif outCodon == codonB:
                                aaList1 = [currAADict[codonB],currAADict[codonA]]
                                aaList2 = [currAADict[codonB],currAADict[codonC]]
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sum2PQ_S += twoPQ1
                                        sum2PQ_N += twoPQ2
                                        synS += 1
                                        nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            con1S += 1
                                            sum2PQ_C1 += twoPQ2
                                        else:
                                            rad1S += 1
                                            sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            con2S += 1
                                            sum2PQ_C2 += twoPQ2
                                        else:
                                            rad2S += 1
                                            sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            con3S += 1
                                            sum2PQ_C3 += twoPQ2
                                        else:
                                            rad3S += 1
                                            sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            con4S += 1
                                            sum2PQ_C4 += twoPQ2
                                        else:
                                            rad4S += 1
                                            sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            con5S += 1
                                            sum2PQ_C5 += twoPQ2
                                        else:
                                            rad5S += 1
                                            sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            con6S += 1
                                            sum2PQ_C6 += twoPQ2
                                        else:
                                            rad6S += 1
                                            sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            con7S += 1
                                            sum2PQ_C7 += twoPQ2
                                        else:
                                            rad7S += 1
                                            sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            meanConS += 1
                                            sum2PQ_meanC += twoPQ2
                                        else:
                                            meanRadS += 1
                                            sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    nsynS += 1
                                    synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sum2PQ_S += twoPQ2
                                    sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ2
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ2
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ2
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ2
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ2
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ2
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ2
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ2
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            elif outCodon == codonC:
                                aaList1 = [currAADict[codonC],currAADict[codonA]]
                                aaList2 = [currAADict[codonC],currAADict[codonB]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sum2PQ_S += twoPQ1
                                        sum2PQ_N += twoPQ2
                                        synS += 1
                                        nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            con1S += 1
                                            sum2PQ_C1 += twoPQ2
                                        else:
                                            rad1S += 1
                                            sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            con2S += 1
                                            sum2PQ_C2 += twoPQ2
                                        else:
                                            rad2S += 1
                                            sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            con3S += 1
                                            sum2PQ_C3 += twoPQ2
                                        else:
                                            rad3S += 1
                                            sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            con4S += 1
                                            sum2PQ_C4 += twoPQ2
                                        else:
                                            rad4S += 1
                                            sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            con5S += 1
                                            sum2PQ_C5 += twoPQ2
                                        else:
                                            rad5S += 1
                                            sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            con6S += 1
                                            sum2PQ_C6 += twoPQ2
                                        else:
                                            rad6S += 1
                                            sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            con7S += 1
                                            sum2PQ_C7 += twoPQ2
                                        else:
                                            rad7S += 1
                                            sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            meanConS += 1
                                            sum2PQ_meanC += twoPQ2
                                        else:
                                            meanRadS += 1
                                            sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    nsynS += 1
                                    synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sum2PQ_S += twoPQ2
                                    sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ1
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ1
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ1
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ1
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ1
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ1
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ1
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ1
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        con1S += 1
                                        sum2PQ_C1 += twoPQ2
                                    else:
                                        rad1S += 1
                                        sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        con2S += 1
                                        sum2PQ_C2 += twoPQ2
                                    else:
                                        rad2S += 1
                                        sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        con3S += 1
                                        sum2PQ_C3 += twoPQ2
                                    else:
                                        rad3S += 1
                                        sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        con4S += 1
                                        sum2PQ_C4 += twoPQ2
                                    else:
                                        rad4S += 1
                                        sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        con5S += 1
                                        sum2PQ_C5 += twoPQ2
                                    else:
                                        rad5S += 1
                                        sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        con6S += 1
                                        sum2PQ_C6 += twoPQ2
                                    else:
                                        rad6S += 1
                                        sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        con7S += 1
                                        sum2PQ_C7 += twoPQ2
                                    else:
                                        rad7S += 1
                                        sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        meanConS += 1
                                        sum2PQ_meanC += twoPQ2
                                    else:
                                        meanRadS += 1
                                        sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            else:
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0])
                                for aa in aaList:
                                    sys.stdout.write(';' + aa + '\tP\tN\n')
                                if len(aaList) > 1:
                                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                                else:
                                    mutType = ''
                                logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                logfile.write('\t' + aaList[0])
                                for aa in aaList:
                                    logfile.write(';' + aa)
                                logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                                
                        else:
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList[0])
                            for aa in aaList:
                                sys.stdout.write(';' + aa + '\tP\tN\n')
                            if len(aaList) > 1:
                                mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                            else:
                                mutType = ''
                            logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            logfile.write('\t' + aaList[0])
                            for aa in aaList:
                                logfile.write(';' + aa)
                            logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                             
                    else:
                        if ab > ac and ab > bc:
                            codonList1 = [codonC,codonB]
                            codonList2 = [codonC,codonA]
                        elif ac > ab and ac > bc:
                            codonList1 = [codonB,codonA]
                            codonList2 = [codonB,codonC]
                        elif bc > ab and bc > ac:
                            codonList1 = [codonA,codonB]
                            codonList2 = [codonA,codonC]
                        aaList1 = []
                        aaList2 = []
                        for comp in codonList1:
                            if i < 3:
                                if comp in startCodons:
                                    aaList1.append('M')
                                else:
                                    aaList1.append(geneticCode[comp])
                            else:
                                aaList1.append(geneticCode[comp])
                        for comp in codonList2:
                            if i < 3:
                                if comp in startCodons:
                                    aaList2.append('M')
                                else:
                                    aaList2.append(geneticCode[comp])
                            else:
                                aaList2.append(geneticCode[comp])
                        if aaList1[0] == aaList1[1]:
                            if aaList2[0] == aaList2[1]:
                                synS += 2
                                twoPQ = 4
                                for allele in currFreqDict:
                                    twoPQ *= currFreqDict[allele]
                                sum2PQ_S += twoPQ
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                for codon in codonList1[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                for codon in codonList2[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                            else:
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                sum2PQ_S += twoPQ1
                                sum2PQ_N += twoPQ2
                                synS += 1
                                nsynS += 1
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                for codon in codonList1[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                for codon in codonList2[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    con1S += 1
                                    sum2PQ_C1 += twoPQ2
                                else:
                                    rad1S += 1
                                    sum2PQ_R1 += twoPQ2
                                if mutType[1] == 0:
                                    con2S += 1
                                    sum2PQ_C2 += twoPQ2
                                else:
                                    rad2S += 1
                                    sum2PQ_R2 += twoPQ2
                                if mutType[2] == 0:
                                    con3S += 1
                                    sum2PQ_C3 += twoPQ2
                                else:
                                    rad3S += 1
                                    sum2PQ_R3 += twoPQ2
                                if mutType[3] == 0:
                                    con4S += 1
                                    sum2PQ_C4 += twoPQ2
                                else:
                                    rad4S += 1
                                    sum2PQ_R4 += twoPQ2
                                if mutType[4] == 0:
                                    con5S += 1
                                    sum2PQ_C5 += twoPQ2
                                else:
                                    rad5S += 1
                                    sum2PQ_R5 += twoPQ2
                                if mutType[5] == 0:
                                    con6S += 1
                                    sum2PQ_C6 += twoPQ2
                                else:
                                    rad6S += 1
                                    sum2PQ_R6 += twoPQ2
                                if mutType[6] == 0:
                                    con7S += 1
                                    sum2PQ_C7 += twoPQ2
                                else:
                                    rad7S += 1
                                    sum2PQ_R7 += twoPQ2
                                if mutType[7] <= 0.5:
                                    meanConS += 1
                                    sum2PQ_meanC += twoPQ2
                                else:
                                    meanRadS += 1
                                    sum2PQ_meanR += twoPQ2
                                for item in mutType[0:-1]:
                                    if item == 0:
                                        sys.stdout.write('\tC')
                                    else:
                                        sys.stdout.write('\tR')
                                sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                        elif aaList2[0] == aaList2[1]:
                            nsynS += 1
                            synS += 1
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                            sum2PQ_S += twoPQ2
                            sum2PQ_N += twoPQ1
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                con1S += 1
                                sum2PQ_C1 += twoPQ1
                            else:
                                rad1S += 1
                                sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                con2S += 1
                                sum2PQ_C2 += twoPQ1
                            else:
                                rad2S += 1
                                sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                con3S += 1
                                sum2PQ_C3 += twoPQ1
                            else:
                                rad3S += 1
                                sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                con4S += 1
                                sum2PQ_C4 += twoPQ1
                            else:
                                rad4S += 1
                                sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                con5S += 1
                                sum2PQ_C5 += twoPQ1
                            else:
                                rad5S += 1
                                sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                con6S += 1
                                sum2PQ_C6 += twoPQ1
                            else:
                                rad6S += 1
                                sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                con7S += 1
                                sum2PQ_C7 += twoPQ1
                            else:
                                rad7S += 1
                                sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                meanConS += 1
                                sum2PQ_meanC += twoPQ1
                            else:
                                meanRadS += 1
                                sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            
                        else:
                            nsynS += 2
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                            sum2PQ_N += twoPQ1 + twoPQ2
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                con1S += 1
                                sum2PQ_C1 += twoPQ1
                            else:
                                rad1S += 1
                                sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                con2S += 1
                                sum2PQ_C2 += twoPQ1
                            else:
                                rad2S += 1
                                sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                con3S += 1
                                sum2PQ_C3 += twoPQ1
                            else:
                                rad3S += 1
                                sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                con4S += 1
                                sum2PQ_C4 += twoPQ1
                            else:
                                rad4S += 1
                                sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                con5S += 1
                                sum2PQ_C5 += twoPQ1
                            else:
                                rad5S += 1
                                sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                con6S += 1
                                sum2PQ_C6 += twoPQ1
                            else:
                                rad6S += 1
                                sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                con7S += 1
                                sum2PQ_C7 += twoPQ1
                            else:
                                rad7S += 1
                                sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                meanConS += 1
                                sum2PQ_meanC += twoPQ1
                            else:
                                meanRadS += 1
                                sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                con1S += 1
                                sum2PQ_C1 += twoPQ2
                            else:
                                rad1S += 1
                                sum2PQ_R1 += twoPQ2
                            if mutType[1] == 0:
                                con2S += 1
                                sum2PQ_C2 += twoPQ2
                            else:
                                rad2S += 1
                                sum2PQ_R2 += twoPQ2
                            if mutType[2] == 0:
                                con3S += 1
                                sum2PQ_C3 += twoPQ2
                            else:
                                rad3S += 1
                                sum2PQ_R3 += twoPQ2
                            if mutType[3] == 0:
                                con4S += 1
                                sum2PQ_C4 += twoPQ2
                            else:
                                rad4S += 1
                                sum2PQ_R4 += twoPQ2
                            if mutType[4] == 0:
                                con5S += 1
                                sum2PQ_C5 += twoPQ2
                            else:
                                rad5S += 1
                                sum2PQ_R5 += twoPQ2
                            if mutType[5] == 0:
                                con6S += 1
                                sum2PQ_C6 += twoPQ2
                            else:
                                rad6S += 1
                                sum2PQ_R6 += twoPQ2
                            if mutType[6] == 0:
                                con7S += 1
                                sum2PQ_C7 += twoPQ2
                            else:
                                rad7S += 1
                                sum2PQ_R7 += twoPQ2
                            if mutType[7] <= 0.5:
                                meanConS += 1
                                sum2PQ_meanC += twoPQ2
                            else:
                                meanRadS += 1
                                sum2PQ_meanR += twoPQ2
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                elif len(currAlleleDict) == 2:
                    currFreqDict = {}
                    twoPQ = 2
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        twoPQ *= freq
                        currFreqDict[codon] = freq
                    if len(aaList) == 1:
                        synS += 2
                        sum2PQ_S += (2*twoPQ)
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                    else:
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\n')
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                        logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        logfile.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
                else:
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN\n')
                    if len(aaList) > 1:
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    else:
                        mutType = ''
                    logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    logfile.write('\t' + aaList[0])
                    for aa in aaList:
                        logfile.write(';' + aa)
                    logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
        i += 1
    logfile.write('\nTotal substitutions\n\n')
    sys.stdout.write('\n\nTotal Substitutions\nGene\tSite\tCodon\tAlleles\tAAs\tPol/Div\tMutation Type\t1\t2\t3\t4\t5\t6\t7\tC/R Index\n')
    codonList = []
    dS = 0
    dN = 0
    dC1 = 0
    dC2 = 0
    dC3 = 0
    dC4 = 0
    dC5 = 0
    dC6 = 0
    dC7 = 0
    dR1 = 0
    dR2 = 0
    dR3 = 0
    dR4 = 0
    dR5 = 0
    dR6 = 0
    dR7 = 0
    dMeanC = 0
    dMeanR = 0
    for site in popInvariantSites:
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i >= start and i <= stop:
                gene = positionDict[locus]
        if site%3 == 0:
            site1 = site
            site2 = site + 1
            site3 = site + 2
        elif site%3 == 1:
            site1 = site - 1
            site2 = site
            site3 = site + 1
        elif site%3 == 2:
            site1 = site - 2
            site2 = site - 1
            site3 = site
        inNuc = refSeq[site]
        outNuc = outSeq[site]
        inSite = refSeq[site1:site3+1]
        outSite = outSeq[site1:site3+1]
        if inNuc != outNuc and 'N' not in inSite and 'N' not in outSite and '-' not in inSite and '-' not in outSite and site/3 not in codonList:
            codonList.append(site/3)
            aaList = []
            if site < 3 and inSite in startCodons:
                aaList.append('M')
                inAA = 'M'
            else:
                aaList.append(geneticCode[inSite])
                inAA = geneticCode[inSite]
            if site < 3 and outSite in startCodons:
                if 'M' not in aaList:
                    aaList.append('M')
                outAA = 'M'
            elif geneticCode[outSite] not in aaList:
                outAA = geneticCode[outSite]
                aaList.append(geneticCode[outSite])
            else:
                outAA = geneticCode[outSite]
            if site1 in popPolymorphicSites or site2 in popPolymorphicSites or site3 in popPolymorphicSites:
                logfile.write('Codon ' + str(1 + (site/3)) + 'has one or more polymorphic sites\n\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\n')
                sys.stdout.write(str(gene) + '\t' + str(site + 1) + '\t' + str((site/3) + 1) + '\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\tD\t\t\t\t\t\t\t\t\t\n')
            else:
                site1List = [inSite[0]]
                site2List = [inSite[1]]
                site3List = [inSite[2]]
                if outSite[0] not in site1List:
                    site1List.append(outSite[0])
                if outSite[1] not in site2List:
                    site2List.append(outSite[1])
                if outSite[2] not in site3List:
                    site3List.append(outSite[2])
                totalChanges = (len(site1List) - 1) + (len(site2List) - 1) + (len(site3List) - 1)
                if totalChanges == 1:
                    sys.stdout.write(str(gene) + '\t' + str(site + 1) + '\t' + str((site/3) + 1) + '\t' + inSite + ';' + outSite)
                    if len(aaList) == 2:
                        dN += 1
                        sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tD\tN')
                        mutType = CRI(aaList)
                        for item in mutType:
                            sys.stdout.write('\t' + str(item))
                        sys.stdout.write('\n')
                        if mutType[0] == 0:
                            dC1 += 1
                        else:
                            dR1 += 1
                        if mutType[1] == 0:
                            dC2 += 1
                        else:
                            dR2 += 1
                        if mutType[2] == 0:
                            dC3 += 1
                        else:
                            dR3 += 1
                        if mutType[3] == 0:
                            dC4 += 1
                        else:
                            dR4 += 1
                        if mutType[4] == 0:
                            dC5 += 1
                        else:
                            dR5 += 1
                        if mutType[5] == 0:
                            dC6 += 1
                        else:
                            dR6 += 1
                        if mutType[6] == 0:
                            dC7 += 1
                        else:
                            dR7 += 1
                        if mutType[7] <= 0.5:
                            dMeanC += 1
                        else:
                            dMeanR += 1
                            
                    else:
                        dS += 1
                        sys.stdout.write('\t-\tD\tS\t-\t-\t-\t-\t-\t-\t-\t-\n')
                else:
                    if len(aaList) == 2:
                        mutType = CRI(aaList)
                        logfile.write('Codon ' + str((site/3) + 1) + ' has a complex evolutionary history\n\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\t' + str(mutType) + '\n')
                        sys.stdout.write(str(gene) + '\t' + str(site + 1) + '\t' + str((site/3) + 1) + '\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\tD\t\t\t\t\t\t\t\t\t\n')
                    else:
                        logfile.write('Codon ' + str((site/3) + 1) + ' has a complex evolutionary history\n\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\n')
                        sys.stdout.write(str(gene) + '\t' + str(site + 1) + '\t' + str((site/3) + 1) + '\t' + inSite + ',' + outSite + '\t' + inAA + ',' + outAA + '\tD\tS\t\t\t\t\t\t\t\t\n')
                        
    sum2PQ_S = str(sum2PQ_S)
    sum2PQ_N = str(sum2PQ_N)
    sum2PQ_C1 = str(sum2PQ_C1)
    sum2PQ_C2 = str(sum2PQ_C2)
    sum2PQ_C3 = str(sum2PQ_C3)
    sum2PQ_C4 = str(sum2PQ_C4)
    sum2PQ_C5 = str(sum2PQ_C5)
    sum2PQ_C6 = str(sum2PQ_C6)
    sum2PQ_C7 = str(sum2PQ_C7)
    sum2PQ_R1 = str(sum2PQ_R1)
    sum2PQ_R2 = str(sum2PQ_R2)
    sum2PQ_R3 = str(sum2PQ_R3)
    sum2PQ_R4 = str(sum2PQ_R4)
    sum2PQ_R5 = str(sum2PQ_R5)
    sum2PQ_R6 = str(sum2PQ_R6)
    sum2PQ_R7 = str(sum2PQ_R7)
    sum2PQ_meanC = str(sum2PQ_meanC)
    sum2PQ_meanR = str(sum2PQ_meanR)
    synS = str(synS)
    nsynS = str(nsynS)
    con1S = str(con1S)
    con2S = str(con2S)
    con3S = str(con3S)
    con4S = str(con4S)
    con5S = str(con5S)
    con6S = str(con6S)
    con7S = str(con7S)
    meanConS = str(meanConS)
    rad1S = str(rad1S)
    rad2S = str(rad2S)
    rad3S = str(rad3S)
    rad4S = str(rad4S)
    rad5S = str(rad5S)
    rad6S = str(rad6S)
    rad7S = str(rad7S)
    meanRadS = str(meanRadS)                
    logfile.write('Sex polymorphisms\n')
    sys.stdout.write('\n\nSex Polymorphisms\nGene\tSite\tCodon\tAlleles\tAAs\tPol/Div\tMutation Type\t1\t2\t3\t4\t5\t6\t7\tC/R Index\t2*pq\n')
    sex_sum2PQ_S = 0
    sex_sum2PQ_N = 0
    sex_sum2PQ_C1 = 0
    sex_sum2PQ_C2 = 0
    sex_sum2PQ_C3 = 0
    sex_sum2PQ_C4 = 0
    sex_sum2PQ_C5 = 0
    sex_sum2PQ_C6 = 0
    sex_sum2PQ_C7 = 0
    sex_sum2PQ_R1 = 0
    sex_sum2PQ_R2 = 0
    sex_sum2PQ_R3 = 0
    sex_sum2PQ_R4 = 0
    sex_sum2PQ_R5 = 0
    sex_sum2PQ_R6 = 0
    sex_sum2PQ_R7 = 0
    sex_sum2PQ_meanC = 0
    sex_sum2PQ_meanR = 0
    sex_synS = 0
    sex_nsynS = 0
    sex_con1S = 0
    sex_con2S = 0
    sex_con3S = 0
    sex_con4S = 0
    sex_con5S = 0
    sex_con6S = 0
    sex_con7S = 0
    sex_meanConS = 0
    sex_rad1S = 0
    sex_rad2S = 0
    sex_rad3S = 0
    sex_rad4S = 0
    sex_rad5S = 0
    sex_rad6S = 0
    sex_rad7S = 0
    sex_meanRadS = 0
    i = 0
    while i < len(codonDict[seqList[0]]):
        outCodon = outCodons[i]
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i*3 >= start and i*3 <= stop:
                gene = positionDict[locus]
        currAlleleDict = {}
        currAlleleList = []
        currAADict = {}
        for seq in sexList:
            currCodons = codonDict[seq]
            currCodon = currCodons[i]
            if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                currAlleleDict[currCodon] = 1
                currAlleleList.append(currCodon)
            elif 'N' not in currCodon and '-' not in currCodon:
                currValue = currAlleleDict[currCodon]
                currValue += 1
                currAlleleDict[currCodon] = currValue
        if len(currAlleleDict) > 1:
            totalIndividuals = 0
            site1 = []
            site2 = []
            site3 = []
            for codon in currAlleleList:
                totalIndividuals += currAlleleDict[codon]
                if codon[0] not in site1:
                    site1.append(codon[0])
                if codon[1] not in site2:
                    site2.append(codon[1])
                if codon[2] not in site3:
                    site3.append(codon[2])
            currFreqDict = {}
            totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
            variableSites = []
            if len(site1) > 1:
                variableSites.append(i*3)
            if len(site2) > 1:
                variableSites.append((i*3) + 1)
            if len(site3) > 1:
                variableSites.append((i*3) + 1)
            aaList = []
            twoPQ = 2
            for codon in currAlleleDict:
                freq = float(currAlleleDict[codon])/totalIndividuals
                currFreqDict[codon] = freq
                if i == 0 and codon in startCodons:
                    aa = 'M'
                else:
                    aa = geneticCode[codon]
                currAADict[codon] = aa
                if aa not in aaList:
                    aaList.append(aa)
            if totalChanges == 1:
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    twoPQ *= freq
                if len(aaList) == 1:
                    sex_synS += 1
                    sex_sum2PQ_S += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                else:
                    sex_nsynS += 1
                    sex_sum2PQ_N += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN')
                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    if mutType[0] == 0:
                        sex_con1S += 1
                        sex_sum2PQ_C1 += twoPQ
                    else:
                        sex_rad1S += 1
                        sex_sum2PQ_R1 += twoPQ
                    if mutType[1] == 0:
                        sex_con2S += 1
                        sex_sum2PQ_C2 += twoPQ
                    else:
                        sex_rad2S += 1
                        sex_sum2PQ_R2 += twoPQ
                    if mutType[2] == 0:
                        sex_con3S += 1
                        sex_sum2PQ_C3 += twoPQ
                    else:
                        sex_rad3S += 1
                        sex_sum2PQ_R3 += twoPQ
                    if mutType[3] == 0:
                        sex_con4S += 1
                        sex_sum2PQ_C4 += twoPQ
                    else:
                        sex_rad4S += 1
                        sex_sum2PQ_R4 += twoPQ
                    if mutType[4] == 0:
                        sex_con5S += 1
                        sex_sum2PQ_C5 += twoPQ
                    else:
                        sex_rad5S += 1
                        sex_sum2PQ_R5 += twoPQ
                    if mutType[5] == 0:
                        sex_con6S += 1
                        sex_sum2PQ_C6 += twoPQ
                    else:
                        sex_rad6S += 1
                        sex_sum2PQ_R6 += twoPQ
                    if mutType[6] == 0:
                        sex_con7S += 1
                        sex_sum2PQ_C7 += twoPQ
                    else:
                        sex_rad7S += 1
                        sex_sum2PQ_R7 += twoPQ
                    if mutType[7] <= 0.5:
                        sex_meanConS += 1
                        sex_sum2PQ_meanC += twoPQ
                    else:
                        sex_meanRadS += 1
                        sex_sum2PQ_meanR += twoPQ
                    for item in mutType[0:-1]:
                        if item == 0:
                            sys.stdout.write('\tC')
                        else:
                            sys.stdout.write('\tR')
                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ) + '\n')
            elif totalChanges == 2:
                if len(currAlleleDict) == 3:
                    ab = 0
                    ac = 0
                    bc = 0
                    codonA = currAlleleList[0]
                    codonB = currAlleleList[1]
                    codonC = currAlleleList[2]
                    
                    if codonA[0] != codonB[0]:
                        ab += 1
                    if codonA[1] != codonB[1]:
                        ab += 1
                    if codonA[2] != codonB[2]:
                        ab += 1
                    if codonA[0] != codonC[0]:
                        ac += 1
                    if codonA[1] != codonC[1]:
                        ac += 1
                    if codonA[2] != codonC[2]:
                        ac += 1
                    if codonC[0] != codonB[0]:
                        bc += 1
                    if codonC[1] != codonB[1]:
                        bc += 1
                    if codonC[2] != codonB[2]:
                        bc += 1
                    if ab == ac and ac == bc:
                        if 'N' not in outCodon and '-' not in outCodon:
                            if outCodon == codonA:
                                aaList1 = [currAADict[codonA],currAADict[codonB]]
                                aaList2 = [currAADict[codonA],currAADict[codonC]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        sex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_S += twoPQ1
                                        sex_sum2PQ_N += twoPQ2
                                        sex_synS += 1
                                        sex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    sex_nsynS += 1
                                    sex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sex_sum2PQ_S += twoPQ2
                                    sex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    sex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ2
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ2
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ2
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ2
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ2
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ2
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ2
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ2
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n') 
                            elif outCodon == codonB:
                                aaList1 = [currAADict[codonB],currAADict[codonA]]
                                aaList2 = [currAADict[codonB],currAADict[codonC]]
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        sex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_S += twoPQ1
                                        sex_sum2PQ_N += twoPQ2
                                        sex_synS += 1
                                        sex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    sex_nsynS += 1
                                    sex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sex_sum2PQ_S += twoPQ2
                                    sex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    sex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ2
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ2
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ2
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ2
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ2
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ2
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ2
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ2
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            elif outCodon == codonC:
                                aaList1 = [currAADict[codonC],currAADict[codonA]]
                                aaList2 = [currAADict[codonC],currAADict[codonB]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        sex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        sex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_S += twoPQ1
                                        sex_sum2PQ_N += twoPQ2
                                        sex_synS += 1
                                        sex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    sex_nsynS += 1
                                    sex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    sex_sum2PQ_S += twoPQ2
                                    sex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    sex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ1
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ1
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ1
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ1
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ1
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ1
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ1
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ1
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ2
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ2
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ2
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ2
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ2
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ2
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ2
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ2
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            else:
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0])
                                for aa in aaList:
                                    sys.stdout.write(';' + aa + '\tP\tN\n')
                                if len(aaList) > 1:
                                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                                else:
                                    mutType = ''
                                logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                logfile.write('\t' + aaList[0])
                                for aa in aaList:
                                    logfile.write(';' + aa)
                                logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                                
                        else:
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList[0])
                            for aa in aaList:
                                sys.stdout.write(';' + aa + '\tP\tN\n')
                            if len(aaList) > 1:
                                mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                            else:
                                mutType = ''
                            logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            logfile.write('\t' + aaList[0])
                            for aa in aaList:
                                logfile.write(';' + aa)
                            logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                             
                    else:
                        if ab > ac and ab > bc:
                            codonList1 = [codonC,codonB]
                            codonList2 = [codonC,codonA]
                        elif ac > ab and ac > bc:
                            codonList1 = [codonB,codonA]
                            codonList2 = [codonB,codonC]
                        elif bc > ab and bc > ac:
                            codonList1 = [codonA,codonB]
                            codonList2 = [codonA,codonC]
                        aaList1 = []
                        aaList2 = []
                        for comp in codonList1:
                            if i < 3:
                                if comp in startCodons:
                                    aaList1.append('M')
                                else:
                                    aaList1.append(geneticCode[comp])
                            else:
                                aaList1.append(geneticCode[comp])
                        for comp in codonList2:
                            if i < 3:
                                if comp in startCodons:
                                    aaList2.append('M')
                                else:
                                    aaList2.append(geneticCode[comp])
                            else:
                                aaList2.append(geneticCode[comp])
                        if aaList1[0] == aaList1[1]:
                            if aaList2[0] == aaList2[1]:
                                sex_synS += 2
                                twoPQ = 4
                                for allele in currFreqDict:
                                    twoPQ *= currFreqDict[allele]
                                sex_sum2PQ_S += twoPQ
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                            else:
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                sex_sum2PQ_S += twoPQ1
                                sex_sum2PQ_N += twoPQ2
                                sex_synS += 1
                                sex_nsynS += 1
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                for codon in codonList1[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                for codon in codonList2[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    sex_con1S += 1
                                    sex_sum2PQ_C1 += twoPQ2
                                else:
                                    sex_rad1S += 1
                                    sex_sum2PQ_R1 += twoPQ2
                                if mutType[1] == 0:
                                    sex_con2S += 1
                                    sex_sum2PQ_C2 += twoPQ2
                                else:
                                    sex_rad2S += 1
                                    sex_sum2PQ_R2 += twoPQ2
                                if mutType[2] == 0:
                                    sex_con3S += 1
                                    sex_sum2PQ_C3 += twoPQ2
                                else:
                                    sex_rad3S += 1
                                    sex_sum2PQ_R3 += twoPQ2
                                if mutType[3] == 0:
                                    sex_con4S += 1
                                    sex_sum2PQ_C4 += twoPQ2
                                else:
                                    sex_rad4S += 1
                                    sex_sum2PQ_R4 += twoPQ2
                                if mutType[4] == 0:
                                    sex_con5S += 1
                                    sex_sum2PQ_C5 += twoPQ2
                                else:
                                    sex_rad5S += 1
                                    sex_sum2PQ_R5 += twoPQ2
                                if mutType[5] == 0:
                                    sex_con6S += 1
                                    sex_sum2PQ_C6 += twoPQ2
                                else:
                                    sex_rad6S += 1
                                    sex_sum2PQ_R6 += twoPQ2
                                if mutType[6] == 0:
                                    sex_con7S += 1
                                    sex_sum2PQ_C7 += twoPQ2
                                else:
                                    sex_rad7S += 1
                                    sex_sum2PQ_R7 += twoPQ2
                                if mutType[7] <= 0.5:
                                    sex_meanConS += 1
                                    sex_sum2PQ_meanC += twoPQ2
                                else:
                                    sex_meanRadS += 1
                                    sex_sum2PQ_meanR += twoPQ2
                                for item in mutType[0:-1]:
                                    if item == 0:
                                        sys.stdout.write('\tC')
                                    else:
                                        sys.stdout.write('\tR')
                                sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                        elif aaList2[0] == aaList2[1]:
                            sex_nsynS += 1
                            sex_synS += 1
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                            sex_sum2PQ_S += twoPQ2
                            sex_sum2PQ_N += twoPQ1
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                sex_con1S += 1
                                sex_sum2PQ_C1 += twoPQ1
                            else:
                                sex_rad1S += 1
                                sex_sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                sex_con2S += 1
                                sex_sum2PQ_C2 += twoPQ1
                            else:
                                sex_rad2S += 1
                                sex_sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                sex_con3S += 1
                                sex_sum2PQ_C3 += twoPQ1
                            else:
                                sex_rad3S += 1
                                sex_sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                sex_con4S += 1
                                sex_sum2PQ_C4 += twoPQ1
                            else:
                                sex_rad4S += 1
                                sex_sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                sex_con5S += 1
                                sex_sum2PQ_C5 += twoPQ1
                            else:
                                sex_rad5S += 1
                                sex_sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                sex_con6S += 1
                                sex_sum2PQ_C6 += twoPQ1
                            else:
                                sex_rad6S += 1
                                sex_sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                sex_con7S += 1
                                sex_sum2PQ_C7 += twoPQ1
                            else:
                                sex_rad7S += 1
                                sex_sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                sex_meanConS += 1
                                sex_sum2PQ_meanC += twoPQ1
                            else:
                                sex_meanRadS += 1
                                sex_sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            
                        else:
                            sex_nsynS += 2
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                            sex_sum2PQ_N += twoPQ1 + twoPQ2
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                sex_con1S += 1
                                sex_sum2PQ_C1 += twoPQ1
                            else:
                                sex_rad1S += 1
                                sex_sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                sex_con2S += 1
                                sex_sum2PQ_C2 += twoPQ1
                            else:
                                sex_rad2S += 1
                                sex_sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                sex_con3S += 1
                                sex_sum2PQ_C3 += twoPQ1
                            else:
                                sex_rad3S += 1
                                sex_sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                sex_con4S += 1
                                sex_sum2PQ_C4 += twoPQ1
                            else:
                                sex_rad4S += 1
                                sex_sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                sex_con5S += 1
                                sex_sum2PQ_C5 += twoPQ1
                            else:
                                sex_rad5S += 1
                                sex_sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                sex_con6S += 1
                                sex_sum2PQ_C6 += twoPQ1
                            else:
                                sex_rad6S += 1
                                sex_sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                sex_con7S += 1
                                sex_sum2PQ_C7 += twoPQ1
                            else:
                                sex_rad7S += 1
                                sex_sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                sex_meanConS += 1
                                sex_sum2PQ_meanC += twoPQ1
                            else:
                                sex_meanRadS += 1
                                sex_sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                sex_con1S += 1
                                sex_sum2PQ_C1 += twoPQ2
                            else:
                                sex_rad1S += 1
                                sex_sum2PQ_R1 += twoPQ2
                            if mutType[1] == 0:
                                sex_con2S += 1
                                sex_sum2PQ_C2 += twoPQ2
                            else:
                                sex_rad2S += 1
                                sex_sum2PQ_R2 += twoPQ2
                            if mutType[2] == 0:
                                sex_con3S += 1
                                sex_sum2PQ_C3 += twoPQ2
                            else:
                                sex_rad3S += 1
                                sex_sum2PQ_R3 += twoPQ2
                            if mutType[3] == 0:
                                sex_con4S += 1
                                sex_sum2PQ_C4 += twoPQ2
                            else:
                                sex_rad4S += 1
                                sex_sum2PQ_R4 += twoPQ2
                            if mutType[4] == 0:
                                sex_con5S += 1
                                sex_sum2PQ_C5 += twoPQ2
                            else:
                                sex_rad5S += 1
                                sex_sum2PQ_R5 += twoPQ2
                            if mutType[5] == 0:
                                sex_con6S += 1
                                sex_sum2PQ_C6 += twoPQ2
                            else:
                                sex_rad6S += 1
                                sex_sum2PQ_R6 += twoPQ2
                            if mutType[6] == 0:
                                sex_con7S += 1
                                sex_sum2PQ_C7 += twoPQ2
                            else:
                                sex_rad7S += 1
                                sex_sum2PQ_R7 += twoPQ2
                            if mutType[7] <= 0.5:
                                sex_meanConS += 1
                                sex_sum2PQ_meanC += twoPQ2
                            else:
                                sex_meanRadS += 1
                                sex_sum2PQ_meanR += twoPQ2
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                elif len(currAlleleDict) == 2:
                    currFreqDict = {}
                    twoPQ = 2
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        twoPQ *= freq
                        currFreqDict[codon] = freq
                    if len(aaList) == 1:
                        sex_synS += 2
                        sex_sum2PQ_S += (2*twoPQ)
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                    else:
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\n')
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                        logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        logfile.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
                else:
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN\n')
                    if len(aaList) > 1:
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    else:
                        mutType = ''
                    logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    logfile.write('\t' + aaList[0])
                    for aa in aaList:
                        logfile.write(';' + aa)
                    logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
        i += 1
    sex_sum2PQ_S = str(sex_sum2PQ_S)
    sex_sum2PQ_N = str(sex_sum2PQ_N)
    sex_sum2PQ_C1 = str(sex_sum2PQ_C1)
    sex_sum2PQ_C2 = str(sex_sum2PQ_C2)
    sex_sum2PQ_C3 = str(sex_sum2PQ_C3)
    sex_sum2PQ_C4 = str(sex_sum2PQ_C4)
    sex_sum2PQ_C5 = str(sex_sum2PQ_C5)
    sex_sum2PQ_C6 = str(sex_sum2PQ_C6)
    sex_sum2PQ_C7 = str(sex_sum2PQ_C7)
    sex_sum2PQ_R1 = str(sex_sum2PQ_R1)
    sex_sum2PQ_R2 = str(sex_sum2PQ_R2)
    sex_sum2PQ_R3 = str(sex_sum2PQ_R3)
    sex_sum2PQ_R4 = str(sex_sum2PQ_R4)
    sex_sum2PQ_R5 = str(sex_sum2PQ_R5)
    sex_sum2PQ_R6 = str(sex_sum2PQ_R6)
    sex_sum2PQ_R7 = str(sex_sum2PQ_R7)
    sex_sum2PQ_meanC = str(sex_sum2PQ_meanC)
    sex_sum2PQ_meanR = str(sex_sum2PQ_meanR)
    sex_synS = str(sex_synS)
    sex_nsynS = str(sex_nsynS)
    sex_con1S = str(sex_con1S)
    sex_con2S = str(sex_con2S)
    sex_con3S = str(sex_con3S)
    sex_con4S = str(sex_con4S)
    sex_con5S = str(sex_con5S)
    sex_con6S = str(sex_con6S)
    sex_con7S = str(sex_con7S)
    sex_meanConS = str(sex_meanConS)
    sex_rad1S = str(sex_rad1S)
    sex_rad2S = str(sex_rad2S)
    sex_rad3S = str(sex_rad3S)
    sex_rad4S = str(sex_rad4S)
    sex_rad5S = str(sex_rad5S)
    sex_rad6S = str(sex_rad6S)
    sex_rad7S = str(sex_rad7S)
    sex_meanRadS = str(sex_meanRadS)
    asex_sum2PQ_S = 0
    asex_sum2PQ_N = 0
    asex_sum2PQ_C1 = 0
    asex_sum2PQ_C2 = 0
    asex_sum2PQ_C3 = 0
    asex_sum2PQ_C4 = 0
    asex_sum2PQ_C5 = 0
    asex_sum2PQ_C6 = 0
    asex_sum2PQ_C7 = 0
    asex_sum2PQ_R1 = 0
    asex_sum2PQ_R2 = 0
    asex_sum2PQ_R3 = 0
    asex_sum2PQ_R4 = 0
    asex_sum2PQ_R5 = 0
    asex_sum2PQ_R6 = 0
    asex_sum2PQ_R7 = 0
    asex_sum2PQ_meanC = 0
    asex_sum2PQ_meanR = 0
    asex_synS = 0
    asex_nsynS = 0
    asex_con1S = 0
    asex_con2S = 0
    asex_con3S = 0
    asex_con4S = 0
    asex_con5S = 0
    asex_con6S = 0
    asex_con7S = 0
    asex_meanConS = 0
    asex_rad1S = 0
    asex_rad2S = 0
    asex_rad3S = 0
    asex_rad4S = 0
    asex_rad5S = 0
    asex_rad6S = 0
    asex_rad7S = 0
    asex_meanRadS = 0
    logfile.write('Asex polymorphisms\n')
    sys.stdout.write('\n\nAsex Polymorphisms\nGene\tSite\tCodon\tAlleles\tAAs\tPol/Div\tMutation Type\t1\t2\t3\t4\t5\t6\t7\tC/R Index\t2*pq\n')
    i = 0
    while i < len(codonDict[seqList[0]]):
        outCodon = outCodons[i]
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i*3 >= start and i*3 <= stop:
                gene = positionDict[locus]
        currAlleleDict = {}
        currAlleleList = []
        currAADict = {}
        for seq in asexList:
            currCodons = codonDict[seq]
            currCodon = currCodons[i]
            if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                currAlleleDict[currCodon] = 1
                currAlleleList.append(currCodon)
            elif 'N' not in currCodon and '-' not in currCodon:
                currValue = currAlleleDict[currCodon]
                currValue += 1
                currAlleleDict[currCodon] = currValue
        if len(currAlleleDict) > 1:
            totalIndividuals = 0
            site1 = []
            site2 = []
            site3 = []
            for codon in currAlleleList:
                totalIndividuals += currAlleleDict[codon]
                if codon[0] not in site1:
                    site1.append(codon[0])
                if codon[1] not in site2:
                    site2.append(codon[1])
                if codon[2] not in site3:
                    site3.append(codon[2])
            currFreqDict = {}
            totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
            variableSites = []
            if len(site1) > 1:
                variableSites.append(i*3)
            if len(site2) > 1:
                variableSites.append((i*3) + 1)
            if len(site3) > 1:
                variableSites.append((i*3) + 1)
            aaList = []
            twoPQ = 2
            for codon in currAlleleDict:
                freq = float(currAlleleDict[codon])/totalIndividuals
                currFreqDict[codon] = freq
                if i == 0 and codon in startCodons:
                    aa = 'M'
                else:
                    aa = geneticCode[codon]
                currAADict[codon] = aa
                if aa not in aaList:
                    aaList.append(aa)
            if totalChanges == 1:
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    twoPQ *= freq
                if len(aaList) == 1:
                    asex_synS += 1
                    asex_sum2PQ_S += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                else:
                    asex_nsynS += 1
                    asex_sum2PQ_N += twoPQ
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN')
                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    if mutType[0] == 0:
                        asex_con1S += 1
                        asex_sum2PQ_C1 += twoPQ
                    else:
                        asex_rad1S += 1
                        asex_sum2PQ_R1 += twoPQ
                    if mutType[1] == 0:
                        asex_con2S += 1
                        asex_sum2PQ_C2 += twoPQ
                    else:
                        asex_rad2S += 1
                        asex_sum2PQ_R2 += twoPQ
                    if mutType[2] == 0:
                        asex_con3S += 1
                        asex_sum2PQ_C3 += twoPQ
                    else:
                        asex_rad3S += 1
                        asex_sum2PQ_R3 += twoPQ
                    if mutType[3] == 0:
                        asex_con4S += 1
                        asex_sum2PQ_C4 += twoPQ
                    else:
                        asex_rad4S += 1
                        asex_sum2PQ_R4 += twoPQ
                    if mutType[4] == 0:
                        asex_con5S += 1
                        asex_sum2PQ_C5 += twoPQ
                    else:
                        asex_rad5S += 1
                        asex_sum2PQ_R5 += twoPQ
                    if mutType[5] == 0:
                        asex_con6S += 1
                        asex_sum2PQ_C6 += twoPQ
                    else:
                        asex_rad6S += 1
                        asex_sum2PQ_R6 += twoPQ
                    if mutType[6] == 0:
                        asex_con7S += 1
                        asex_sum2PQ_C7 += twoPQ
                    else:
                        asex_rad7S += 1
                        asex_sum2PQ_R7 += twoPQ
                    if mutType[7] <= 0.5:
                        asex_meanConS += 1
                        asex_sum2PQ_meanC += twoPQ
                    else:
                        asex_meanRadS += 1
                        asex_sum2PQ_meanR += twoPQ
                    for item in mutType[0:-1]:
                        if item == 0:
                            sys.stdout.write('\tC')
                        else:
                            sys.stdout.write('\tR')
                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ) + '\n')
            elif totalChanges == 2:
                if len(currAlleleDict) == 3:
                    ab = 0
                    ac = 0
                    bc = 0
                    codonA = currAlleleList[0]
                    codonB = currAlleleList[1]
                    codonC = currAlleleList[2]
                    
                    if codonA[0] != codonB[0]:
                        ab += 1
                    if codonA[1] != codonB[1]:
                        ab += 1
                    if codonA[2] != codonB[2]:
                        ab += 1
                    if codonA[0] != codonC[0]:
                        ac += 1
                    if codonA[1] != codonC[1]:
                        ac += 1
                    if codonA[2] != codonC[2]:
                        ac += 1
                    if codonC[0] != codonB[0]:
                        bc += 1
                    if codonC[1] != codonB[1]:
                        bc += 1
                    if codonC[2] != codonB[2]:
                        bc += 1
                    if ab == ac and ac == bc:
                        if 'N' not in outCodon and '-' not in outCodon:
                            if outCodon == codonA:
                                aaList1 = [currAADict[codonA],currAADict[codonB]]
                                aaList2 = [currAADict[codonA],currAADict[codonC]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        asex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        asex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_S += twoPQ1
                                        asex_sum2PQ_N += twoPQ2
                                        asex_synS += 1
                                        asex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    asex_nsynS += 1
                                    asex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    asex_sum2PQ_S += twoPQ2
                                    asex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    asex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    asex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ2
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ2
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ2
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ2
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ2
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ2
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ2
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ2
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n') 
                            elif outCodon == codonB:
                                aaList1 = [currAADict[codonB],currAADict[codonA]]
                                aaList2 = [currAADict[codonB],currAADict[codonC]]
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        asex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        asex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_S += twoPQ1
                                        asex_sum2PQ_N += twoPQ2
                                        asex_synS += 1
                                        asex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    asex_nsynS += 1
                                    asex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    asex_sum2PQ_S += twoPQ2
                                    asex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    asex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    asex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ2
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ2
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ2
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ2
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ2
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ2
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ2
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ2
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            elif outCodon == codonC:
                                aaList1 = [currAADict[codonC],currAADict[codonA]]
                                aaList2 = [currAADict[codonC],currAADict[codonB]]
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                                if aaList1[0] == aaList1[1]:
                                    if aaList2[0] == aaList2[1]:
                                        asex_synS += 2
                                        twoPQ = 4
                                        for allele in currFreqDict:
                                            twoPQ *= currFreqDict[allele]
                                        asex_sum2PQ_S += twoPQ
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                        for codon in currAlleleList[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                    else:
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_S += twoPQ1
                                        asex_sum2PQ_N += twoPQ2
                                        asex_synS += 1
                                        asex_nsynS += 1
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                        for codon in codonList1[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                        for codon in codonList2[1:]:
                                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                        sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                                        for item in mutType[0:-1]:
                                            if item == 0:
                                                sys.stdout.write('\tC')
                                            else:
                                                sys.stdout.write('\tR')
                                        sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                                elif aaList2[0] == aaList2[1]:
                                    asex_nsynS += 1
                                    asex_synS += 1
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                    asex_sum2PQ_S += twoPQ2
                                    asex_sum2PQ_N += twoPQ1
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                        
                                else:
                                    asex_nsynS += 2
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    asex_sum2PQ_N += twoPQ1 + twoPQ2
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                    for codon in codonList1[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ1
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ1
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ1
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ1
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ1
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ1
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ1
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ1
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ1
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ1
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ1
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ1
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ1
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ1
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ1
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ1
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                    for codon in codonList2[1:]:
                                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ2
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ2
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ2
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ2
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ2
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ2
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ2
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ2
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ2
                                    for item in mutType[0:-1]:
                                        if item == 0:
                                            sys.stdout.write('\tC')
                                        else:
                                            sys.stdout.write('\tR')
                                    sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                            else:
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0])
                                for aa in aaList:
                                    sys.stdout.write(';' + aa + '\tP\tN\n')
                                if len(aaList) > 1:
                                    mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                                else:
                                    mutType = ''
                                logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                logfile.write('\t' + aaList[0])
                                for aa in aaList:
                                    logfile.write(';' + aa)
                                logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                                
                        else:
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList[0])
                            for aa in aaList:
                                sys.stdout.write(';' + aa + '\tP\tN\n')
                            if len(aaList) > 1:
                                mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                            else:
                                mutType = ''
                            logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                            for codon in currAlleleList[1:]:
                                logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            logfile.write('\t' + aaList[0])
                            for aa in aaList:
                                logfile.write(';' + aa)
                            logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')                             
                    else:
                        if ab > ac and ab > bc:
                            codonList1 = [codonC,codonB]
                            codonList2 = [codonC,codonA]
                        elif ac > ab and ac > bc:
                            codonList1 = [codonB,codonA]
                            codonList2 = [codonB,codonC]
                        elif bc > ab and bc > ac:
                            codonList1 = [codonA,codonB]
                            codonList2 = [codonA,codonC]
                        aaList1 = []
                        aaList2 = []
                        for comp in codonList1:
                            if i < 3:
                                if comp in startCodons:
                                    aaList1.append('M')
                                else:
                                    aaList1.append(geneticCode[comp])
                            else:
                                aaList1.append(geneticCode[comp])
                        for comp in codonList2:
                            if i < 3:
                                if comp in startCodons:
                                    aaList2.append('M')
                                else:
                                    aaList2.append(geneticCode[comp])
                            else:
                                aaList2.append(geneticCode[comp])
                        if aaList1[0] == aaList1[1]:
                            if aaList2[0] == aaList2[1]:
                                asex_synS += 2
                                twoPQ = 4
                                for allele in currFreqDict:
                                    twoPQ *= currFreqDict[allele]
                                asex_sum2PQ_S += twoPQ
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                                for codon in currAlleleList[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                            else:
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                asex_sum2PQ_S += twoPQ1
                                asex_sum2PQ_N += twoPQ2
                                asex_synS += 1
                                asex_nsynS += 1
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                                for codon in codonList1[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList1[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ1) + '\n')
                                sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                                for codon in codonList2[1:]:
                                    sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                                sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                                mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    asex_con1S += 1
                                    asex_sum2PQ_C1 += twoPQ2
                                else:
                                    asex_rad1S += 1
                                    asex_sum2PQ_R1 += twoPQ2
                                if mutType[1] == 0:
                                    asex_con2S += 1
                                    asex_sum2PQ_C2 += twoPQ2
                                else:
                                    asex_rad2S += 1
                                    asex_sum2PQ_R2 += twoPQ2
                                if mutType[2] == 0:
                                    asex_con3S += 1
                                    asex_sum2PQ_C3 += twoPQ2
                                else:
                                    asex_rad3S += 1
                                    asex_sum2PQ_R3 += twoPQ2
                                if mutType[3] == 0:
                                    asex_con4S += 1
                                    asex_sum2PQ_C4 += twoPQ2
                                else:
                                    asex_rad4S += 1
                                    asex_sum2PQ_R4 += twoPQ2
                                if mutType[4] == 0:
                                    asex_con5S += 1
                                    asex_sum2PQ_C5 += twoPQ2
                                else:
                                    asex_rad5S += 1
                                    asex_sum2PQ_R5 += twoPQ2
                                if mutType[5] == 0:
                                    asex_con6S += 1
                                    asex_sum2PQ_C6 += twoPQ2
                                else:
                                    asex_rad6S += 1
                                    asex_sum2PQ_R6 += twoPQ2
                                if mutType[6] == 0:
                                    asex_con7S += 1
                                    asex_sum2PQ_C7 += twoPQ2
                                else:
                                    asex_rad7S += 1
                                    asex_sum2PQ_R7 += twoPQ2
                                if mutType[7] <= 0.5:
                                    asex_meanConS += 1
                                    asex_sum2PQ_meanC += twoPQ2
                                else:
                                    asex_meanRadS += 1
                                    asex_sum2PQ_meanR += twoPQ2
                                for item in mutType[0:-1]:
                                    if item == 0:
                                        sys.stdout.write('\tC')
                                    else:
                                        sys.stdout.write('\tR')
                                sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                        elif aaList2[0] == aaList2[1]:
                            asex_nsynS += 1
                            asex_synS += 1
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                            asex_sum2PQ_S += twoPQ2
                            asex_sum2PQ_N += twoPQ1
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ2) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                asex_con1S += 1
                                asex_sum2PQ_C1 += twoPQ1
                            else:
                                asex_rad1S += 1
                                asex_sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                asex_con2S += 1
                                asex_sum2PQ_C2 += twoPQ1
                            else:
                                asex_rad2S += 1
                                asex_sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                asex_con3S += 1
                                asex_sum2PQ_C3 += twoPQ1
                            else:
                                asex_rad3S += 1
                                asex_sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                asex_con4S += 1
                                asex_sum2PQ_C4 += twoPQ1
                            else:
                                asex_rad4S += 1
                                asex_sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                asex_con5S += 1
                                asex_sum2PQ_C5 += twoPQ1
                            else:
                                asex_rad5S += 1
                                asex_sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                asex_con6S += 1
                                asex_sum2PQ_C6 += twoPQ1
                            else:
                                asex_rad6S += 1
                                asex_sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                asex_con7S += 1
                                asex_sum2PQ_C7 += twoPQ1
                            else:
                                asex_rad7S += 1
                                asex_sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                asex_meanConS += 1
                                asex_sum2PQ_meanC += twoPQ1
                            else:
                                asex_meanRadS += 1
                                asex_sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            
                        else:
                            asex_nsynS += 2
                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                            asex_sum2PQ_N += twoPQ1 + twoPQ2
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList1[0] + ',freq=' + str(currFreqDict[codonList1[0]]))
                            for codon in codonList1[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                asex_con1S += 1
                                asex_sum2PQ_C1 += twoPQ1
                            else:
                                asex_rad1S += 1
                                asex_sum2PQ_R1 += twoPQ1
                            if mutType[1] == 0:
                                asex_con2S += 1
                                asex_sum2PQ_C2 += twoPQ1
                            else:
                                asex_rad2S += 1
                                asex_sum2PQ_R2 += twoPQ1
                            if mutType[2] == 0:
                                asex_con3S += 1
                                asex_sum2PQ_C3 += twoPQ1
                            else:
                                asex_rad3S += 1
                                asex_sum2PQ_R3 += twoPQ1
                            if mutType[3] == 0:
                                asex_con4S += 1
                                asex_sum2PQ_C4 += twoPQ1
                            else:
                                asex_rad4S += 1
                                asex_sum2PQ_R4 += twoPQ1
                            if mutType[4] == 0:
                                asex_con5S += 1
                                asex_sum2PQ_C5 += twoPQ1
                            else:
                                asex_rad5S += 1
                                asex_sum2PQ_R5 += twoPQ1
                            if mutType[5] == 0:
                                asex_con6S += 1
                                asex_sum2PQ_C6 += twoPQ1
                            else:
                                asex_rad6S += 1
                                asex_sum2PQ_R6 += twoPQ1
                            if mutType[6] == 0:
                                asex_con7S += 1
                                asex_sum2PQ_C7 += twoPQ1
                            else:
                                asex_rad7S += 1
                                asex_sum2PQ_R7 += twoPQ1
                            if mutType[7] <= 0.5:
                                asex_meanConS += 1
                                asex_sum2PQ_meanC += twoPQ1
                            else:
                                asex_meanRadS += 1
                                asex_sum2PQ_meanR += twoPQ1
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ1) + '\n')
                            sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + codonList2[0] + ',freq=' + str(currFreqDict[codonList2[0]]))
                            for codon in codonList2[1:]:
                                sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                            sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN')
                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                            if mutType[0] == 0:
                                asex_con1S += 1
                                asex_sum2PQ_C1 += twoPQ2
                            else:
                                asex_rad1S += 1
                                asex_sum2PQ_R1 += twoPQ2
                            if mutType[1] == 0:
                                asex_con2S += 1
                                asex_sum2PQ_C2 += twoPQ2
                            else:
                                asex_rad2S += 1
                                asex_sum2PQ_R2 += twoPQ2
                            if mutType[2] == 0:
                                asex_con3S += 1
                                asex_sum2PQ_C3 += twoPQ2
                            else:
                                asex_rad3S += 1
                                asex_sum2PQ_R3 += twoPQ2
                            if mutType[3] == 0:
                                asex_con4S += 1
                                asex_sum2PQ_C4 += twoPQ2
                            else:
                                asex_rad4S += 1
                                asex_sum2PQ_R4 += twoPQ2
                            if mutType[4] == 0:
                                asex_con5S += 1
                                asex_sum2PQ_C5 += twoPQ2
                            else:
                                asex_rad5S += 1
                                asex_sum2PQ_R5 += twoPQ2
                            if mutType[5] == 0:
                                asex_con6S += 1
                                asex_sum2PQ_C6 += twoPQ2
                            else:
                                asex_rad6S += 1
                                asex_sum2PQ_R6 += twoPQ2
                            if mutType[6] == 0:
                                asex_con7S += 1
                                asex_sum2PQ_C7 += twoPQ2
                            else:
                                asex_rad7S += 1
                                asex_sum2PQ_R7 += twoPQ2
                            if mutType[7] <= 0.5:
                                asex_meanConS += 1
                                asex_sum2PQ_meanC += twoPQ2
                            else:
                                asex_meanRadS += 1
                                asex_sum2PQ_meanR += twoPQ2
                            for item in mutType[0:-1]:
                                if item == 0:
                                    sys.stdout.write('\tC')
                                else:
                                    sys.stdout.write('\tR')
                            sys.stdout.write('\t' +str(mutType[-1]) + '\t' + str(twoPQ2) + '\n')
                elif len(currAlleleDict) == 2:
                    currFreqDict = {}
                    twoPQ = 2
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        twoPQ *= freq
                        currFreqDict[codon] = freq
                    if len(aaList) == 1:
                        asex_synS += 2
                        asex_sum2PQ_S += (2*twoPQ)
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + '\tP\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(twoPQ) + '\n')
                    else:
                        sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        sys.stdout.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\n')
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                        logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                        for codon in currAlleleList[1:]:
                            logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                        logfile.write('\t' + aaList[0] + ';' + aaList[1] + '\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
                else:
                    sys.stdout.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        sys.stdout.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    sys.stdout.write('\t' + aaList2[0] + ';' + aaList2[1] + '\tP\tN\n')
                    if len(aaList) > 1:
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                    else:
                        mutType = ''
                    logfile.write(str(gene) + '\t' + str(variableSites[0] + 1) + '\t' + str(i + 1) + '\t' + currAlleleList[0] + ',freq=' + str(currFreqDict[currAlleleList[0]]))
                    for codon in currAlleleList[1:]:
                        logfile.write(';' + codon + ',freq=' + str(currFreqDict[codon]))
                    logfile.write('\t' + aaList[0])
                    for aa in aaList:
                        logfile.write(';' + aa)
                    logfile.write('\tP\tN\t' + str(mutType) + '\t' + outCodon + '\n')
        i += 1
    asex_sum2PQ_S = str(asex_sum2PQ_S)
    asex_sum2PQ_N = str(asex_sum2PQ_N)
    asex_sum2PQ_C1 = str(asex_sum2PQ_C1)
    asex_sum2PQ_C2 = str(asex_sum2PQ_C2)
    asex_sum2PQ_C3 = str(asex_sum2PQ_C3)
    asex_sum2PQ_C4 = str(asex_sum2PQ_C4)
    asex_sum2PQ_C5 = str(asex_sum2PQ_C5)
    asex_sum2PQ_C6 = str(asex_sum2PQ_C6)
    asex_sum2PQ_C7 = str(asex_sum2PQ_C7)
    asex_sum2PQ_R1 = str(asex_sum2PQ_R1)
    asex_sum2PQ_R2 = str(asex_sum2PQ_R2)
    asex_sum2PQ_R3 = str(asex_sum2PQ_R3)
    asex_sum2PQ_R4 = str(asex_sum2PQ_R4)
    asex_sum2PQ_R5 = str(asex_sum2PQ_R5)
    asex_sum2PQ_R6 = str(asex_sum2PQ_R6)
    asex_sum2PQ_R7 = str(asex_sum2PQ_R7)
    asex_sum2PQ_meanC = str(asex_sum2PQ_meanC)
    asex_sum2PQ_meanR = str(asex_sum2PQ_meanR)
    asex_synS = str(asex_synS)
    asex_nsynS = str(asex_nsynS)
    asex_con1S = str(asex_con1S)
    asex_con2S = str(asex_con2S)
    asex_con3S = str(asex_con3S)
    asex_con4S = str(asex_con4S)
    asex_con5S = str(asex_con5S)
    asex_con6S = str(asex_con6S)
    asex_con7S = str(asex_con7S)
    asex_meanConS = str(asex_meanConS)
    asex_rad1S = str(asex_rad1S)
    asex_rad2S = str(asex_rad2S)
    asex_rad3S = str(asex_rad3S)
    asex_rad4S = str(asex_rad4S)
    asex_rad5S = str(asex_rad5S)
    asex_rad6S = str(asex_rad6S)
    asex_rad7S = str(asex_rad7S)
    asex_meanRadS = str(asex_meanRadS)
    summaryFile = open('mt_conRad_summary.txt','w')
    summaryFile.write('\tS\tN\tmeanC\tmeanR\tC1\tR1\tC2\tR2\tC3\tR3\tC4\tR4\tC5\tR5\tC6\tR6\tC7\tR7\nP.antipodarum-P.estuarinus\t' + str(dS) + '\t' + str(dN) + '\t' + str(dMeanC) + '\t' + str(dMeanR) + '\t' + str(dC1) + '\t' + str(dR1) + '\t' + str(dC2) + '\t' + str(dR2) + '\t' + str(dC3) + '\t' + str(dR3) + '\t' + str(dC4) + '\t' + str(dR4) + '\t' + str(dC5) + '\t' + str(dR5) + '\t' + str(dC6) + '\t' + str(dR6) + '\t' + str(dC7) + '\t' + str(dR7) + '\nP.antipodarum-P.estuarinus Sites\nP.antipodarum-P.estuarinus D\nP.antipodarum-P.estuarinus k (JC-corrected)\nP. antipodarum-P.estuarinus var(k)\n\nP. antipodarum\t' + synS + '\t' + nsynS + '\t' + meanConS + '\t' + meanRadS + '\t' + con1S + '\t' + rad1S + '\t' + con2S + '\t' + rad2S + '\t' + con3S + '\t' + rad3S + '\t' + con4S + '\t' + rad4S + '\t' + con5S + '\t' + rad5S + '\t' + con6S + '\t' + rad6S + '\t' + con7S + '\t' + rad7S + '\n')
    summaryFile.write('P.antipodarum Sites\nP.antipodarum sum(2*pq)\t' + sum2PQ_S + '\t' + sum2PQ_N + '\t' + sum2PQ_meanC + '\t' + sum2PQ_meanR + '\t' + sum2PQ_C1 + '\t' + sum2PQ_R1 + '\t' + sum2PQ_C2 + '\t' + sum2PQ_R2 + '\t' + sum2PQ_C3 + '\t' + sum2PQ_R3 + '\t' + sum2PQ_C4 + '\t' + sum2PQ_R4 + '\t' + sum2PQ_C5 + '\t' + sum2PQ_R5 + '\t' + sum2PQ_C6 + '\t' + sum2PQ_R6 + '\t' + sum2PQ_C7 + '\t' + sum2PQ_R7 + '\n')
    summaryFile.write('P.antipodarum π\nP.antipodarum π/πS\nP. antipodarum aN\nP. antipodarum theta\nP.antipodarum theta/thetaS\n\n')
    summaryFile.write('Sex\t' + sex_synS + '\t' + sex_nsynS + '\t' + sex_meanConS + '\t' + sex_meanRadS + '\t' + sex_con1S + '\t' + sex_rad1S + '\t' + sex_con2S + '\t' + sex_rad2S + '\t' + sex_con3S + '\t' + sex_rad3S + '\t' + sex_con4S + '\t' + sex_rad4S + '\t' + sex_con5S + '\t' + sex_rad5S + '\t' + sex_con6S + '\t' + sex_rad6S + '\t' + sex_con7S + '\t' + sex_rad7S + '\n')
    summaryFile.write('Sex Sites\nSex sum(2*pq)\t' + sex_sum2PQ_S + '\t' + sex_sum2PQ_N + '\t' + sex_sum2PQ_meanC + '\t' + sex_sum2PQ_meanR + '\t' + sex_sum2PQ_C1 + '\t' + sex_sum2PQ_R1 + '\t' + sex_sum2PQ_C2 + '\t' + sex_sum2PQ_R2 + '\t' + sex_sum2PQ_C3 + '\t' + sex_sum2PQ_R3 + '\t' + sex_sum2PQ_C4 + '\t' + sex_sum2PQ_R4 + '\t' + sex_sum2PQ_C5 + '\t' + sex_sum2PQ_R5 + '\t' + sex_sum2PQ_C6 + '\t' + sex_sum2PQ_R6 + '\t' + sex_sum2PQ_C7 + '\t' + sex_sum2PQ_R7 + '\n')
    summaryFile.write('Sex π\nSex π/πS\nSex aN\nSex theta\nSex theta/thetaS\n\n')
    summaryFile.write('Asex\t' + asex_synS + '\t' + asex_nsynS + '\t' + asex_meanConS + '\t' + asex_meanRadS + '\t' + asex_con1S + '\t' + asex_rad1S + '\t' + asex_con2S + '\t' + asex_rad2S + '\t' + asex_con3S + '\t' + asex_rad3S + '\t' + asex_con4S + '\t' + asex_rad4S + '\t' + asex_con5S + '\t' + asex_rad5S + '\t' + asex_con6S + '\t' + asex_rad6S + '\t' + asex_con7S + '\t' + asex_rad7S + '\n')
    summaryFile.write('Asex Sites\nAsex sum(2*pq)\t' + asex_sum2PQ_S + '\t' + asex_sum2PQ_N + '\t' + asex_sum2PQ_meanC + '\t' + asex_sum2PQ_meanR + '\t' + asex_sum2PQ_C1 + '\t' + asex_sum2PQ_R1 + '\t' + asex_sum2PQ_C2 + '\t' + asex_sum2PQ_R2 + '\t' + asex_sum2PQ_C3 + '\t' + asex_sum2PQ_R3 + '\t' + asex_sum2PQ_C4 + '\t' + asex_sum2PQ_R4 + '\t' + asex_sum2PQ_C5 + '\t' + asex_sum2PQ_R5 + '\t' + asex_sum2PQ_C6 + '\t' + asex_sum2PQ_R6 + '\t' + asex_sum2PQ_C7 + '\t' + asex_sum2PQ_R7 + '\n')
    summaryFile.write('Asex π\nAsex π/πS\nAsex aN\nAsex theta\nAsex theta/thetaS\n\n')  
    summaryFile.close()
    logfile.close()      

def CRI(aaList):
    aaSchemeList = [1,2,3,4,5,6,7]
    aaSchemeDict = {1:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"C",("A","Y"):"C",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"C",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"C",("N","Y"):"C",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"C",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"C",("C","Y"):"C",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"C",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"C",("G","Y"):"C",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"C",("I","Y"):"C",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"C",("L","Y"):"C",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"C",("M","Y"):"C",("M","V"):"C",("F","P"):"C",("F","S"):"C",("F","T"):"C",("F","W"):"C",("F","Y"):"C",("F","V"):"C",("P","S"):"C",("P","T"):"C",("P","W"):"C",("P","Y"):"C",("P","V"):"C",("S","T"):"C",("S","W"):"C",("S","Y"):"C",("S","V"):"C",("T","W"):"C",("T","Y"):"C",("T","V"):"C",("W","Y"):"C",("W","V"):"C",("Y","V"):"C",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"C",("Y","A"):"C",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"C",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"C",("Y","N"):"C",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"C",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"C",("Y","C"):"C",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"C",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"C",("Y","G"):"C",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"C",("Y","I"):"C",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"C",("Y","L"):"C",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"C",("Y","M"):"C",("V","M"):"C",("P","F"):"C",("S","F"):"C",("T","F"):"C",("W","F"):"C",("Y","F"):"C",("V","F"):"C",("S","P"):"C",("T","P"):"C",("W","P"):"C",("Y","P"):"C",("V","P"):"C",("T","S"):"C",("W","S"):"C",("Y","S"):"C",("V","S"):"C",("W","T"):"C",("Y","T"):"C",("V","T"):"C",("Y","W"):"C",("V","W"):"C",("V","Y"):"C",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},2:{("R","H"):"C",("R","K"):"C",("R","D"):"C",("R","E"):"C",("R","A"):"R",("R","N"):"C",("R","C"):"C",("R","Q"):"C",("R","G"):"C",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"C",("R","T"):"C",("R","W"):"R",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"C",("H","E"):"C",("H","A"):"R",("H","N"):"C",("H","C"):"C",("H","Q"):"C",("H","G"):"C",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"C",("H","T"):"C",("H","W"):"R",("H","Y"):"C",("H","V"):"R",("K","D"):"C",("K","E"):"C",("K","A"):"R",("K","N"):"C",("K","C"):"C",("K","Q"):"C",("K","G"):"C",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"C",("K","T"):"C",("K","W"):"R",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"C",("D","Q"):"C",("D","G"):"C",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"C",("D","T"):"C",("D","W"):"R",("D","Y"):"C",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"C",("E","Q"):"C",("E","G"):"C",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"C",("E","T"):"C",("E","W"):"R",("E","Y"):"C",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"C",("E","R"):"C",("A","R"):"R",("N","R"):"C",("C","R"):"C",("Q","R"):"C",("G","R"):"C",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"C",("T","R"):"C",("W","R"):"R",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"C",("E","H"):"C",("A","H"):"R",("N","H"):"C",("C","H"):"C",("Q","H"):"C",("G","H"):"C",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"C",("T","H"):"C",("W","H"):"R",("Y","H"):"C",("V","H"):"R",("D","K"):"C",("E","K"):"C",("A","K"):"R",("N","K"):"C",("C","K"):"C",("Q","K"):"C",("G","K"):"C",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"C",("T","K"):"C",("W","K"):"R",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"C",("Q","D"):"C",("G","D"):"C",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"C",("T","D"):"C",("W","D"):"R",("Y","D"):"C",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"C",("Q","E"):"C",("G","E"):"C",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"C",("T","E"):"C",("W","E"):"R",("Y","E"):"C",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},3:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"R",("D","Q"):"C",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"R",("E","Q"):"C",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"R",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"R",("N","T"):"R",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"R",("C","T"):"R",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"C",("F","T"):"C",("F","W"):"R",("F","Y"):"R",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"R",("Q","D"):"C",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"R",("Q","E"):"C",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"R",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"R",("T","N"):"R",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"R",("T","C"):"R",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"C",("T","F"):"C",("W","F"):"R",("Y","F"):"R",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},4:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"C",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"C",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"C",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"C",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"C",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"C",("H","Y"):"C",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"C",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"C",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"C",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"C",("N","Q"):"R",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"C",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"C",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"C",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"C",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"C",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"C",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"C",("Y","H"):"C",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"C",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"C",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"C",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"C",("Q","N"):"R",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"C",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},5:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"R",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"C",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"R",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"C",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},6:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"R",("G","T"):"R",("G","W"):"C",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"R",("T","G"):"R",("W","G"):"C",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},7:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}}
    resultsList = []
    cri = 0
    for scheme in aaSchemeList:
        currScheme = aaSchemeDict[scheme]
        currValue = currScheme[(aaList[0],aaList[1])]
        if currValue == 'R':
            cri += 1
            resultsList.append(1)
        else:
            resultsList.append(0)
    cri = cri/7.0
    resultsList.append(cri)
    return resultsList
            
        
                
        
        
def buildCodonDict(fasta):
    code = 'invertebrateMt'
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG']
    seqDict,seqList = buildSeqDict(fasta)
    codonDict = {}
    AADict = {}
    for seq in seqList:
        nucleotideSeq = seqDict[seq]
        codonList = []
        i = 2
        while i < len(nucleotideSeq):
            currCodon = nucleotideSeq[i-2] + nucleotideSeq[i-1] + nucleotideSeq[i]
            codonList.append(currCodon)
            i += 3
        codonDict[seq] = codonList
        AAseq = ''
        codonNum = 1
        for codon in codonList:
            if codonNum == 1 and 'N' not in codon and '-' not in codon:
                if codon in startCodons:
                    aa = 'M'
                else:
                    aa = geneticCode[codon]
            elif 'N' not in codon and '-' not in codon:
                aa = geneticCode[codon]
            else:
                aa = 'X'
            AAseq += aa
            codonNum += 1
        if AAseq[-1] == '*':
            AAseq = AAseq[0:-1]
        AADict[seq] = AAseq
    return seqDict, seqList, codonDict

def buildSeqDict(fasta):
    infile = open(fasta,'r')
    scaffoldDict = {}
    scaffoldList = []
    seqName = ''
    currSeq = ''
    for line in infile:
        if line[0] == '>':
            if seqName != '':
                scaffoldDict[seqName] = currSeq
            seqName = line
            while seqName[-1] == '\n' or seqName[-1] == '\t' or seqName[-1] == '\r':
                seqName = seqName[0:-1]
            scaffoldList.append(seqName)
            currSeq = ''
        else:
            currSeq += line
            while currSeq[-1] == '\n' or currSeq[-1] == '\t' or currSeq[-1] == '\r':
                currSeq = currSeq[0:-1]
    scaffoldDict[seqName] = currSeq 
    return scaffoldDict, scaffoldList

def meanSites(fasta):
    asexList = ['>$Duluth','>$Heron2','>$McGregor','>$Waik36','>$WalesC','>$clone_1','>$AC51','>$Heron_mitochondrion','>$clone_7','>$Waik37','>$Gunn','>$DenmarkA','>$Waik372','>$Tarawera','>$Poerua_triploid','>$Kaniere_triploid','>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237','>$Brunner_2_4n','>$Brunner_6_3n','>$Grasmere_1_4n','>$Grasmere_6_3n','>$Poerua_72_4n','>$Rotoiti_1_4n']
    sexList = ['>$Kaniere_1_2n','>$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309','>$Yellow_Contig_56','>$Alexsex','>$AlexMap','>$Lady','>$Ianthe','>$Rotoroa_1_2n']
    antipodarumList = ['>$Duluth','>$Heron2','>$McGregor','>$Waik36','>$WalesC','>$clone_1','>$AC51','>$Heron_mitochondrion','>$clone_7','>$Waik37','>$Gunn','>$DenmarkA','>$Waik372','>$Tarawera','>$Poerua_triploid','>$Kaniere_triploid','>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237','>$Brunner_2_4n','>$Brunner_6_3n','>$Grasmere_1_4n','>$Grasmere_6_3n','>$Poerua_72_4n','>$Rotoiti_1_4n','>$Kaniere_1_2n','>$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309','>$Yellow_Contig_56','>$Alexsex','>$AlexMap','>$Lady','>$Ianthe','>$Rotoroa_1_2n']
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    sexS = 0
    sexN = 0
    meanC = 0
    meanR = 0
    sexMeanC = 0
    sexMeanR = 0
    asexMeanC = 0
    asexMeanR = 0
    sexC1 = 0
    sexR1 = 0
    sexC2 = 0
    sexR2 = 0
    sexC3 = 0
    sexR3 = 0
    sexC4 = 0
    sexR4 = 0
    sexC5 = 0
    sexR5 = 0
    sexC6 = 0
    sexR6 = 0
    sexC7 = 0
    sexR7 = 0
    asexS = 0
    asexN = 0
    asexC1 = 0
    asexR1 = 0
    asexC2 = 0
    asexR2 = 0
    asexC3 = 0
    asexR3 = 0
    asexC4 = 0
    asexR4 = 0
    asexC5 = 0
    asexR5 = 0
    asexC6 = 0
    asexR6 = 0
    asexC7 = 0
    asexR7 = 0
    S = 0
    N = 0
    C1 = 0
    R1 = 0
    C2 = 0
    R2 = 0
    C3 = 0
    R3 = 0
    C4 = 0
    R4 = 0
    C5 = 0
    R5 = 0
    C6 = 0
    R6 = 0
    C7 = 0
    R7 = 0
    est = countSites(codonDict['>Potamopyrgus_estuarinus']) #[totalSynSites,totalNonsynSites,totalMeanCSites,totalMeanRSites,totalC1Sites,totalR1Sites,totalC2Sites,totalR2Sites,totalC3Sites,totalR3Sites,totalC4Sites,totalR4Sites,totalC5Sites,totalR5Sites,totalC6Sites,totalR6Sites,totalC7Sites,totalR7Sites]
    estS = est[0]
    estN = est[1]
    estMeanC = est[2]
    estMeanR = est[3]
    estC1 = est[4]
    estR1 = est[5]
    estC2 = est[6]
    estR2 = est[7]
    estC3 = est[8]
    estR3 = est[9]
    estC4 = est[10]
    estR4 = est[11]
    estC5 = est[12]
    estR5 = est[13]
    estC6 = est[14]
    estR6 = est[15]
    estC7 = est[16]
    estR7 =  est[17]
    for item in est:
        print str(item) + '\t'
    '''outfile = open('sites.txt','w')
    for snail in antipodarumList:
        snailSites = countSites(codonDict[snail])#[totalSynSites,totalNonsynSites,totalMeanCSites,totalMeanRSites,totalC1Sites,totalR1Sites,totalC2Sites,totalR2Sites,totalC3Sites,totalR3Sites,totalC4Sites,totalR4Sites,totalC5Sites,totalR5Sites,totalC6Sites,totalR6Sites,totalC7Sites,totalR7Sites]
        sys.stdout.write(snail)
        for item in snailSites:
            sys.stdout.write('\t' + str(item))
        sys.stdout.write('\n')
        S += snailSites[0]
        N += snailSites[1]
        C1 += snailSites[4]
        R1 += snailSites[5]
        C2 += snailSites[6]
        R2 += snailSites[7]
        C3 += snailSites[8]
        R3 += snailSites[9]
        C4 += snailSites[10]
        R4 += snailSites[11]
        C5 += snailSites[12]
        R5 += snailSites[13]
        C6 += snailSites[14]
        R6 += snailSites[15]
        C7 += snailSites[16]
        R7 += snailSites[17]
        meanC += snailSites[2]
        meanR += snailSites[3]
        if snail in sexList:
            sexS += snailSites[0]
            sexN += snailSites[1]
            sexMeanC += snailSites[2]
            sexMeanR += snailSites[3]
            sexC1 += snailSites[4]
            sexR1 += snailSites[5]
            sexC2 += snailSites[6]
            sexR2 += snailSites[7]
            sexC3 += snailSites[8]
            sexR3 += snailSites[9]
            sexC4 += snailSites[10]
            sexR4 += snailSites[11]
            sexC5 += snailSites[12]
            sexR5 += snailSites[13]
            sexC6 += snailSites[14]
            sexR6 += snailSites[15]
            sexC7 += snailSites[16]
            sexR7 += snailSites[17]
        elif snail in asexList:
            asexS += snailSites[0]
            asexN += snailSites[1]
            asexMeanC += snailSites[2]
            asexMeanR += snailSites[3]
            asexC1 += snailSites[4]
            asexR1 += snailSites[5]
            asexC2 += snailSites[6]
            asexR2 += snailSites[7]
            asexC3 += snailSites[8]
            asexR3 += snailSites[9]
            asexC4 += snailSites[10]
            asexR4 += snailSites[11]
            asexC5 += snailSites[12]
            asexR5 += snailSites[13]
            asexC6 += snailSites[14]
            asexR6 += snailSites[15]
            asexC7 += snailSites[16]
            asexR7 += snailSites[17]
    sexS /= len(sexList)
    sexN /= len(sexList)
    sexMeanC /= len(sexList)
    sexMeanR /= len(sexList)
    sexC1 /= len(sexList)
    sexR1 /= len(sexList)
    sexC2 /= len(sexList)
    sexR2 /= len(sexList)
    sexC3 /= len(sexList)
    sexR3 /= len(sexList)
    sexC4 /= len(sexList)
    sexR4 /= len(sexList)
    sexC5 /= len(sexList)
    sexR5 /= len(sexList)
    sexC6 /= len(sexList)
    sexR6 /= len(sexList)
    sexC7 /= len(sexList)
    sexR7 /= len(sexList)
    asexS /= len(asexList)
    asexN /= len(asexList)
    sexMeanC /= len(sexList)
    sexMeanR /= len(sexList)
    asexC1 /= len(asexList)
    asexR1 /= len(asexList)
    asexC2 /= len(asexList)
    asexR2 /= len(asexList)
    asexC3 /= len(asexList)
    asexR3 /= len(asexList)
    asexC4 /= len(asexList)
    asexR4 /= len(asexList)
    asexC5 /= len(asexList)
    asexR5 /= len(asexList)
    asexC6 /= len(asexList)
    asexR6 /= len(asexList)
    asexC7 /= len(asexList)
    asexR7 /= len(asexList)
    asexMeanC /= len(asexList)
    asexMeanR /= len(asexList)
    divS = (S + estS)/(len(antipodarumList) + 1)
    divN = (N + estN)/(len(antipodarumList) + 1)
    divMeanC = (meanC + estMeanC)/(len(antipodarumList) + 1)
    divMeanR = (meanR + estMeanR)/(len(antipodarumList) + 1)
    divC1 = (C1 + estC1)/(len(antipodarumList) + 1)
    divR1 = (R1 + estR1)/(len(antipodarumList) + 1)
    divC2 = (C2 + estC2)/(len(antipodarumList) + 1)
    divR2 = (R2 + estR2)/(len(antipodarumList) + 1)
    divC3 = (C3 + estC3)/(len(antipodarumList) + 1)
    divR3 = (R3 + estR3)/(len(antipodarumList) + 1)
    divC4 = (C4 + estC4)/(len(antipodarumList) + 1)
    divR4 = (R4 + estR4)/(len(antipodarumList) + 1)
    divC5 = (C5 + estC5)/(len(antipodarumList) + 1)
    divR5 = (R5 + estR5)/(len(antipodarumList) + 1)
    divC6 = (C6 + estC6)/(len(antipodarumList) + 1)
    divR6 = (R6 + estR6)/(len(antipodarumList) + 1)
    divC7 = (C7 + estC7)/(len(antipodarumList) + 1)
    divR7 = (R7 + estR7)/(len(antipodarumList) + 1)
    S /= len(antipodarumList)
    N /= len(antipodarumList)
    meanC /= len(antipodarumList)
    meanR /= len(antipodarumList)
    C1 /= len(antipodarumList)
    R1 /= len(antipodarumList)
    C2 /= len(antipodarumList)
    R2 /= len(antipodarumList)
    C3 /= len(antipodarumList)
    R3 /= len(antipodarumList)
    C4 /= len(antipodarumList)
    R4 /= len(antipodarumList)
    C5 /= len(antipodarumList)
    R5 /= len(antipodarumList)
    C6 /= len(antipodarumList)
    R6 /= len(antipodarumList)
    C7 /= len(antipodarumList)
    R7 /= len(antipodarumList)
    outfile.write('Group\tS\tN\tmeanC\tmeanR\tC1\tR1\tC2\tR2\tC3\tR3\tC4\tR4\tC5\tR5\tC6\tR6\tC7\tR7\nP.antipodarum-P.estuarinus\t' + str(divS) + '\t' + str(divN) + '\t' + str(divMeanC) + '\t' + str(divMeanR) + '\t' + str(divC1) + '\t' + str(divR1) + '\t' + str(divC2) + '\t' + str(divR2) + '\t' + str(divC3) + '\t' + str(divR3) + '\t' + str(divC4) + '\t' + str(divR4) + '\t' + str(divC5) + '\t' + str(divR5) + '\t' + str(divC6) + '\t' + str(divR6) + '\t' + str(divC7) + '\t' + str(divR7) + '\nP.antipodarum\t' + str(S) + '\t' + str(N) + '\t' + str(meanC) + '\t' + str(meanR) + '\t' + str(C1) + '\t' + str(R1) + '\t' + str(C2) + '\t' + str(R2) + '\t' + str(C3) + '\t' + str(R3) + '\t' + str(C4) + '\t' + str(R4) + '\t' + str(C5) + '\t' + str(R5) + '\t' + str(C6) + '\t' + str(R6) + '\t' + str(C7) + '\t' + str(R7) + '\nSex\t' + str(sexS) + '\t' + str(sexN) + '\t' + str(sexMeanC) + '\t' + str(sexMeanR) + '\t' + str(sexC1) + '\t' + str(sexR1) + '\t' + str(sexC2) + '\t' + str(sexR2) + '\t' + str(sexC3) + '\t' + str(sexR3) + '\t' + str(sexC4) + '\t' + str(sexR4) + '\t' + str(sexC5) + '\t' + str(sexR5) + '\t' + str(sexC6) + '\t' + str(sexR6) + '\t' + str(sexC7) + '\t' + str(sexR7) + '\nAsex\t' + str(asexS) + '\t' + str(asexN) + '\t' + str(asexMeanC) + '\t' + str(asexMeanR) + '\t' + str(asexC1) + '\t' + str(asexR1) + '\t' + str(asexC2) + '\t' + str(asexR2) + '\t' + str(asexC3) + '\t' + str(asexR3) + '\t' + str(asexC4) + '\t' + str(asexR4) + '\t' + str(asexC5) + '\t' + str(asexR5) + '\t' + str(asexC6) + '\t' + str(asexR6) + '\t' + str(asexC7) + '\t' + str(asexR7) + '\n')
    outfile.close()'''

def countSites(codonList):
    code = 'invertebrateMt'
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt cod
    aaSchemeDict1 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"C",("A","Y"):"C",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"C",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"C",("N","Y"):"C",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"C",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"C",("C","Y"):"C",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"C",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"C",("G","Y"):"C",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"C",("I","Y"):"C",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"C",("L","Y"):"C",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"C",("M","Y"):"C",("M","V"):"C",("F","P"):"C",("F","S"):"C",("F","T"):"C",("F","W"):"C",("F","Y"):"C",("F","V"):"C",("P","S"):"C",("P","T"):"C",("P","W"):"C",("P","Y"):"C",("P","V"):"C",("S","T"):"C",("S","W"):"C",("S","Y"):"C",("S","V"):"C",("T","W"):"C",("T","Y"):"C",("T","V"):"C",("W","Y"):"C",("W","V"):"C",("Y","V"):"C",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"C",("Y","A"):"C",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"C",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"C",("Y","N"):"C",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"C",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"C",("Y","C"):"C",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"C",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"C",("Y","G"):"C",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"C",("Y","I"):"C",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"C",("Y","L"):"C",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"C",("Y","M"):"C",("V","M"):"C",("P","F"):"C",("S","F"):"C",("T","F"):"C",("W","F"):"C",("Y","F"):"C",("V","F"):"C",("S","P"):"C",("T","P"):"C",("W","P"):"C",("Y","P"):"C",("V","P"):"C",("T","S"):"C",("W","S"):"C",("Y","S"):"C",("V","S"):"C",("W","T"):"C",("Y","T"):"C",("V","T"):"C",("Y","W"):"C",("V","W"):"C",("V","Y"):"C",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict2 = {("R","H"):"C",("R","K"):"C",("R","D"):"C",("R","E"):"C",("R","A"):"R",("R","N"):"C",("R","C"):"C",("R","Q"):"C",("R","G"):"C",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"C",("R","T"):"C",("R","W"):"R",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"C",("H","E"):"C",("H","A"):"R",("H","N"):"C",("H","C"):"C",("H","Q"):"C",("H","G"):"C",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"C",("H","T"):"C",("H","W"):"R",("H","Y"):"C",("H","V"):"R",("K","D"):"C",("K","E"):"C",("K","A"):"R",("K","N"):"C",("K","C"):"C",("K","Q"):"C",("K","G"):"C",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"C",("K","T"):"C",("K","W"):"R",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"C",("D","Q"):"C",("D","G"):"C",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"C",("D","T"):"C",("D","W"):"R",("D","Y"):"C",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"C",("E","Q"):"C",("E","G"):"C",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"C",("E","T"):"C",("E","W"):"R",("E","Y"):"C",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"C",("E","R"):"C",("A","R"):"R",("N","R"):"C",("C","R"):"C",("Q","R"):"C",("G","R"):"C",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"C",("T","R"):"C",("W","R"):"R",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"C",("E","H"):"C",("A","H"):"R",("N","H"):"C",("C","H"):"C",("Q","H"):"C",("G","H"):"C",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"C",("T","H"):"C",("W","H"):"R",("Y","H"):"C",("V","H"):"R",("D","K"):"C",("E","K"):"C",("A","K"):"R",("N","K"):"C",("C","K"):"C",("Q","K"):"C",("G","K"):"C",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"C",("T","K"):"C",("W","K"):"R",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"C",("Q","D"):"C",("G","D"):"C",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"C",("T","D"):"C",("W","D"):"R",("Y","D"):"C",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"C",("Q","E"):"C",("G","E"):"C",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"C",("T","E"):"C",("W","E"):"R",("Y","E"):"C",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict3 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"R",("D","Q"):"C",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"R",("E","Q"):"C",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"R",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"R",("N","T"):"R",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"R",("C","T"):"R",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"C",("F","T"):"C",("F","W"):"R",("F","Y"):"R",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"R",("Q","D"):"C",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"R",("Q","E"):"C",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"R",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"R",("T","N"):"R",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"R",("T","C"):"R",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"C",("T","F"):"C",("W","F"):"R",("Y","F"):"R",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict4 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"C",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"C",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"C",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"C",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"C",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"C",("H","Y"):"C",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"C",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"C",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"C",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"C",("N","Q"):"R",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"C",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"C",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"C",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"C",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"C",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"C",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"C",("Y","H"):"C",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"C",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"C",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"C",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"C",("Q","N"):"R",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"C",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict5 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"R",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"C",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"R",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"C",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict6 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"R",("G","T"):"R",("G","W"):"C",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"R",("T","G"):"R",("W","G"):"C",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict7 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    totalSynSites = 0.0
    totalNonsynSites = 0.0
    totalC1Sites = 0.0
    totalR1Sites = 0.0
    totalC2Sites = 0.0
    totalR2Sites = 0.0
    totalC3Sites = 0.0
    totalR3Sites = 0.0
    totalC4Sites = 0.0
    totalR4Sites = 0.0
    totalC5Sites = 0.0
    totalR5Sites = 0.0
    totalC6Sites = 0.0
    totalR6Sites = 0.0
    totalC7Sites = 0.0
    totalR7Sites = 0.0
    totalMeanCSites = 0.0
    totalMeanRSites = 0.0
    codonNum = 0
    for codon in codonList:
        if 'N' in codon or '-' in codon:
            totalSynSites += 0.729166667
            totalNonsynSites += 2.270833333
            totalC1Sites += 1.395833333	
            totalR1Sites += 0.875	
            totalC2Sites += 1.270833333	
            totalR2Sites += 1	
            totalC3Sites += 0.708333333	
            totalR3Sites += 1.5625	
            totalC4Sites += 0.895833333	
            totalR4Sites += 1.375	
            totalC5Sites += 1.0625	
            totalR5Sites += 1.208333333	
            totalC6Sites += 0.854166667	
            totalR6Sites += 1.416666667	
            totalC7Sites += 0.8125	
            totalR7Sites += 1.458333333
            totalMeanCSites += 1.0 
            totalMeanRSites += 1.270833333
        else:
            currS = 0.0
            currN = 0.0
            currC1 = 0.0
            currC2 = 0.0
            currC3 = 0.0
            currC4 = 0.0
            currC5 = 0.0
            currC6 = 0.0
            currC7 = 0.0
            currR1 = 0.0
            currR2 = 0.0
            currR3 = 0.0
            currR4 = 0.0
            currR5 = 0.0
            currR6 = 0.0
            currR7 = 0.0
            currMeanC = 0.0
            currMeanR = 0.0
            site1 = codon[0]
            site2 = codon[1]
            site3 = codon[2]
            if site1 == 'A':
                mut1 = 'C' + site2 + site3
                mut2 = 'G' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'C':
                mut1 = 'A' + site2 + site3
                mut2 = 'G' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'G':
                mut1 = 'A' + site2 + site3
                mut2 = 'C' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'T':
                mut1 = 'A' + site2 + site3
                mut2 = 'C' + site2 + site3
                mut3 = 'G' + site2 + site3
            if site2 == 'A':
                mut4 = site1 + 'C' + site3
                mut5 = site1 + 'G' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'C':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'G' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'G':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'C' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'T':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'C' + site3
                mut6 = site1 + 'G' + site3
            if site3 == 'A':
                mut7 = site1 + site2 + 'C'
                mut8 = site1 + site2 + 'G'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'C':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'G'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'G':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'C'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'T':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'C'
                mut9 = site1 + site2 + 'G'
            if codonNum == 0:
                aaList = []
                if codon in startCodons:
                    currAA = 'M'
                else:
                    currAA = geneticCode[codon]
                if mut1 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut1])
                if mut2 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut2])
                if mut3 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut3])
                if mut4 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut4])
                if mut5 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut5])
                if mut6 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut6])
                if mut7 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut7])
                if mut8 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut8])
                if mut9 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut9])
            else:
                aaList = [geneticCode[mut1],geneticCode[mut2],geneticCode[mut3], geneticCode[mut4],geneticCode[mut5],geneticCode[mut6],geneticCode[mut7],geneticCode[mut8],geneticCode[mut9]]
                currAA = geneticCode[codon]
            for aa in aaList:
                if aa == currAA:
                    currS += 1.0
                else:
                    currN += 1.0
                    conRad1 = aaSchemeDict1[(currAA,aa)]
                    conRad2 = aaSchemeDict2[(currAA,aa)]
                    conRad3 = aaSchemeDict3[(currAA,aa)]
                    conRad4 = aaSchemeDict4[(currAA,aa)]
                    conRad5 = aaSchemeDict5[(currAA,aa)]
                    conRad6 = aaSchemeDict6[(currAA,aa)]
                    conRad7 = aaSchemeDict7[(currAA,aa)]
                    meanConRad = CRI([currAA,aa])
                    if meanConRad[7] > 0.5:
                        meanConRad = 'R'
                    else:
                        meanConRad = 'C'
                    if conRad1 == 'R':
                        currR1 += 1
                    else:
                        currC1 += 1
                    if conRad2 == 'R':
                        currR2 += 1
                    else:
                        currC2 += 1
                    if conRad3 == 'R':
                        currR3 += 1
                    else:
                        currC3 += 1
                    if conRad4 == 'R':
                        currR4 += 1
                    else:
                        currC4 += 1
                    if conRad5 == 'R':
                        currR5 += 1
                    else:
                        currC5 += 1
                    if conRad6 == 'R':
                        currR6 += 1
                    else:
                        currC6 += 1
                    if conRad7 == 'R':
                        currR7 += 1
                    else:
                        currC7 += 1
                    if meanConRad == 'R':
                        currMeanR += 1
                    else:
                        currMeanC += 1
            currS /= 3.0
            currN /= 3.0
            currC1 /= 3.0
            currC2 /= 3.0
            currC3 /= 3.0
            currC4 /= 3.0
            currC5 /= 3.0
            currC6 /= 3.0
            currC7 /= 3.0
            currMeanC /= 3.0
            currR1 /= 3.0
            currR2 /= 3.0
            currR3 /= 3.0
            currR4 /= 3.0
            currR5 /= 3.0
            currR6 /= 3.0
            currR7 /= 3.0
            currMeanR /= 3.0
            totalSynSites += currS
            totalNonsynSites += currN
            totalC1Sites += currC1
            totalR1Sites += currR1
            totalC2Sites += currC2
            totalR2Sites += currR2
            totalC3Sites += currC3
            totalR3Sites += currR3
            totalC4Sites += currC4
            totalR4Sites += currR4
            totalC5Sites += currC5
            totalR5Sites += currR5
            totalC6Sites += currC6
            totalR6Sites += currR6
            totalC7Sites += currC7
            totalR7Sites += currR7
            totalMeanCSites += currMeanC
            totalMeanRSites += currMeanR
            codonNum += 1
    return [totalSynSites,totalNonsynSites,totalMeanCSites,totalMeanRSites,totalC1Sites,totalR1Sites,totalC2Sites,totalR2Sites,totalC3Sites,totalR3Sites,totalC4Sites,totalR4Sites,totalC5Sites,totalR5Sites,totalC6Sites,totalR6Sites,totalC7Sites,totalR7Sites]

def mapChanges(fasta):
    #cladeDict = {'A': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237',  '>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309',  '>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC',  '>$Brunner_2_4n'], 'B': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC',  '>$Brunner_2_4n'], 'C': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC'], 'D': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36'], 'E': ['>$Waik37', '>$Waik372', '>$Tarawera', '>$Kaniere_triploid'], 'F': ['>$Waik37', '>$Waik372', '>$Tarawera'], 'G': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237',  '>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309'], 'H': ['>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309'], 'I': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237'], 'J': ['>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237'], 'K': ['>$clone_7', '>$DenmarkA', '>$Duluth'], 'L': ['>$clone_7', '>$DenmarkA'], 'M': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56'], 'N': ['>$*AlexMap', '>$*Alexsex', '>$*Yellow_Contig_56'], 'O': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n'], 'P': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n'], 'Q': ['>$*Lady', '>$Grasmere_1_4n', '>$*Kaniere_1_2n'], 'R': ['>$*Lady', '>$Grasmere_1_4n'], 'S': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn'], 'T': ['>$McGregor', '>$Poerua_72_4n', '>$Gunn'], 'U': ['>$McGregor', '>$Poerua_72_4n'], 'V': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n'], 'W': ['>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid'], 'X': ['>$AC51', '>$Heron_mitochondrion', '>$Grasmere_6_3n'], 'Y': ['>$Heron2', '>$clone_1', '>$Rotoiti_1_4n'], 'Z': ['>$Heron2', '>$clone_1']}
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    cladeList = ['H','L','R','U','Z','F','K','N','Q','T','Y','X','E','J','W','D','C','B','V','S','P','O','M','I','G','A']
    popList = []
    sexList = []
    outList = [] 
    asexList = []
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
            if '*' in seq:
                sexList.append(seq)
            else:
                asexList.append(seq)
        else:
            outList.append(seq)
    outSeq = seqDict[outList[0]]
    sys.stdout.write('Asex Polymorphisms\nGene\tSite\tCodon\tLineages w/ Derived Allele\t# Individuals w/ derived allele\tAlleles\tP. est\n')
    i = 0
    while i < len(seqDict[seqList[0]]):
        outNuc = outSeq[i]
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i >= start and i <= stop:
                gene = positionDict[locus]
        currAlleleDict = {}
        currAlleleList = []
        for seq in asexList:
            currSeq = seqDict[seq]
            currNuc = currSeq[i]
            if currNuc not in currAlleleDict and 'N' != currNuc and '-' != currNuc:
                currAlleleDict[currNuc] = [seq]
                currAlleleList.append(currNuc)
            elif 'N' != currNuc and '-' != currNuc:
                currList = currAlleleDict[currNuc]
                currList.append(seq)
                currAlleleDict[currNuc] = currList
        if len(currAlleleDict) > 1:
            for nuc in currAlleleList:
                if nuc != outNuc:
                    #currCladeList = cladeList
                    currList = currAlleleDict[nuc]
                    '''for group in cladeList:
                        compClade = cladeDict[group]
                        removeClade = False
                        for lineage in currList:
                            if lineage not in compClade:
                                removeClade = True
                        if removeClade == True:
                            currCladeList.remove(group)
                    print currCladeList
                    if len(currAlleleDict[nuc]) > 1:
                        sys.stdout.write(gene + '\t' + str(i + 1) + '\t' + str((i*3)+1) + '\t' + str(currAlleleDict[nuc]) + '\t' + str(len(currAlleleDict[nuc])) + '\t' + str(currAlleleList) + '\t' + outNuc + '\n')
                    else:'''
                    sys.stdout.write(gene + '\t' + str(i + 1) + '\t' + str((i*3)+1) + '\t' + str(currAlleleDict[nuc]) + '\t' + str(len(currAlleleDict[nuc])) + '\t' + str(currAlleleList) + '\t' + outNuc + '\n')
        i += 1
    
            
def foldedSFS(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    asexList = []
    logfile = open(fasta[0:-5] + '_foldedSFS.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
            if '*' in seq:
                sexList.append(seq)
            else:
                asexList.append(seq)
        else:
            outList.append(seq)
    refSeq = seqDict[sexList[0]]
    sys.stdout.write('Site\tCodon Position\tCodon Number\tAllele List\tAA List\tType of Change\t1\t2\t3\t4\t5\t6\t7\tC/R Index\t# Individuals w/ Minor Allele\n')
    for site in range(len(refSeq)):
        codonNum = site/3
        pos = (site+1)%3
        if pos == 1:
            nucPos = 1
        elif pos == 2:
            nucPos = 2
        elif pos == 0:
            nucPos = 3
        currAlleleDict = {}
        currAlleleList = []
        for seq in asexList:
            currSeq = seqDict[seq]
            currNuc = currSeq[site]
            if currNuc not in currAlleleList and currNuc != 'N' and currNuc != '-':
                currAlleleList.append(currNuc)
                currAlleleDict[currNuc] = 1
            elif currNuc != 'N' and currNuc != '-':
                currValue = currAlleleDict[currNuc] + 1
                currAlleleDict[currNuc] = currValue
        if len(currAlleleDict) == 2:
            currCodonDict = {}
            currCodonList = []
            for seq in asexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[codonNum]
                if 'N' not in currCodon and '-' not in currCodon and currCodon not in currCodonList:
                    currCodonList.append(currCodon)
                    currCodonDict[currCodon] = 1
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currCodonDict[currCodon] + 1
                    currCodonDict[currCodon] = currValue
            currAAList = []
            for codon in currCodonList:
                if codonNum == 0:
                    if codon in startCodons:
                        if 'M' not in currAAList:
                            currAAList.append('M')
                    else:
                        if geneticCode[codon] not in currAAList:
                            currAAList.append(geneticCode[codon])
                elif geneticCode[codon] not in currAAList:
                    currAAList.append(geneticCode[codon])
            if len(currAAList) == 1:
                if currAlleleDict[currAlleleList[1]] < currAlleleDict[currAlleleList[0]]:
                    currMin = currAlleleList[1]
                else:
                    currMin = currAlleleList[0]
                sys.stdout.write(str(site + 1) + '\t' + str(nucPos) + '\t' + str(codonNum + 1) + '\t' + str(currAlleleList) + '\t' + currAAList[0] + '\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(currAlleleDict[currMin]) + '\n')
            elif len(currCodonDict) == 2:
                if currAlleleDict[currAlleleList[1]] < currAlleleDict[currAlleleList[0]]:
                    currMin = currAlleleList[1]
                else:
                    currMin = currAlleleList[0]
                mutType = CRI(currAAList)
                sys.stdout.write(str(site + 1) + '\t' + str(nucPos) + '\t' + str(codonNum + 1) + '\t' + str(currAlleleList) + '\t' + str(currAAList) + '\tN\t' + str(mutType[0]) + '\t' + str(mutType[1]) + '\t' + str(mutType[2]) + '\t' + str(mutType[3]) + '\t' + str(mutType[4]) + '\t' + str(mutType[5]) + '\t' + str(mutType[6]) + '\t' + str(mutType[7]) + '\t' + str(currAlleleDict[currMin]) + '\n')
            else:
                currMax = currCodonDict[currCodonList[0]]
                maxCodon = currCodonList[0]
                currMin = currCodonDict[currCodonList[0]]
                minCodon = currCodonList[0]
                for codon in currCodonList[1:]:
                    if currCodonDict[codon] >= currMax:
                        currMax = currCodonDict[codon]
                        maxCodon = codon
                    elif currCodonDict[codon] <= currMin:
                        currMin = currCodonDict[codon]
                        minCodon = codon
                newAAList = []
                if codonNum == 0:
                    if maxCodon in startCodons:
                        newAAList.append('M')
                    else:
                        newAAList.append(geneticCode[maxCodon])
                    if minCodon not in startCodons:
                        newAAList.append(geneticCode[minCodon])
                else:
                    newAAList.append(geneticCode[maxCodon])
                    if geneticCode[minCodon] not in newAAList:
                        newAAList.append(geneticCode[minCodon])
                if len(newAAList) == 2:
                    mutType = CRI(newAAList)
                    sys.stdout.write(str(site + 1) + '\t' + str(nucPos) + '\t' + str(codonNum + 1) + '\t' + str(currAlleleList) + '\t' + str(newAAList) + '\tN\t' + str(mutType[0]) + '\t' + str(mutType[1]) + '\t' + str(mutType[2]) + '\t' + str(mutType[3]) + '\t' + str(mutType[4]) + '\t' + str(mutType[5]) + '\t' + str(mutType[6]) + '\t' + str(mutType[7]) + '\t' + str(currCodonDict[minCodon]) + '\n')
                else:
                    sys.stdout.write(str(site + 1) + '\t' + str(nucPos) + '\t' + str(codonNum + 1) + '\t' + str(currAlleleList) + '\t' + newAAList[0] + '\tS\t-\t-\t-\t-\t-\t-\t-\t-\t' + str(currCodonDict[minCodon]) + '\n')
                    
        elif len(currAlleleList) > 2:
            currCodonDict = {}
            currCodonList = []
            for seq in asexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[codonNum]
                if 'N' not in currCodon and '-' not in currCodon and currCodon not in currCodonList:
                    currCodonList.append(currCodon)
                    currCodonDict[currCodon] = 1
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currCodonDict[currCodon] + 1
                    currCodonDict[currCodon] = currValue
            currAAList = []
            for codon in currCodonList:
                if codonNum == 0:
                    if codon in startCodons:
                        if 'M' not in currAAList:
                            currAAList.append('M')
                    else:
                        if geneticCode[codon] not in currAAList:
                            currAAList.append(geneticCode[codon])
                elif geneticCode[codon] not in currAAList:
                    currAAList.append(geneticCode[codon])
            logfile.write(str(site + 1) + '\t' + str(nucPos) + '\t' + str(codonNum + 1) + '\t' + str(currCodonDict) + '\t' + str(currAAList) + '\n')
    logfile.close()

def numSingletons(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    synSites = {">$Duluth":2591.52083333,	">$Heron2":2598,	">$McGregor":2599,	">$Waik36":2586.91666667,	">$WalesC":2584.91666667,	">$clone_1":2598,	">$AC51":2598.33333333,	">$Heron_mitochondrion":2599,	">$clone_7":2592.85416667,	">$Waik37":2586.58333333,	">$Gunn":2597.66666667,	">$DenmarkA":2593.125,	">$Waik372":2589.25,	">$Tarawera":2586.58333333,	">$Poerua_triploid":2597,	">$Kaniere_triploid":2586.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2593.79166667,	">$Brunner_2_4n":2593.60416674,	">$Brunner_6_3n":2592.9583334,	">$Grasmere_1_4n":2628.66666703,	">$Grasmere_6_3n":2599.62500001,	">$Poerua_72_4n":2605.47916675,	">$Rotoiti_1_4n":2594.35416672,	">$*Kaniere_1_2n":2598.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2595,	">$*Yellow_Contig_56":2592.33333333,	">$*Alexsex":2592.33333333,	">$*AlexMap":2592.33333333,	">$*Lady":2598.66666667,	">$*Ianthe":2597,	">$*Rotoroa_1_2n":2598.58333338}
    C1Sites = {">$Duluth":6323.85416667,	">$Heron2":6320.33333333,	">$McGregor":6319,	">$Waik36":6330.25,	">$WalesC":6333.25,	">$clone_1":6319.66666667,	">$AC51":6318.66666667,	">$Heron_mitochondrion":6319.33333333,	">$clone_7":6322.52083333,	">$Waik37":6327.25,	">$Gunn":6324.33333333,	">$DenmarkA":6322.45833333,	">$Waik372":6330.58333333,	">$Tarawera":6329.25,	">$Poerua_triploid":6321.66666667,	">$Kaniere_triploid":6330.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":6320.125,	">$Brunner_2_4n":6259.27083326,	">$Brunner_6_3n":6262.95833327,	">$Grasmere_1_4n":5990.99999963,	">$Grasmere_6_3n":6307.62499999,	">$Poerua_72_4n":6232.81249992,	">$Rotoiti_1_4n":6264.68749995,	">$*Kaniere_1_2n":6320.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":6321,	">$*Yellow_Contig_56":6326.33333333,	">$*Alexsex":6326.33333333,	">$*AlexMap":6326.33333333,	">$*Lady":6318,	">$*Ianthe":6321.33333333,	">$*Rotoroa_1_2n":6271.58333329}
    R1Sites = {">$Duluth":2298.625,	">$Heron2":2295.66666667,	">$McGregor":2296,	">$Waik36":2296.83333333,	">$WalesC":2295.83333333,	">$clone_1":2296.33333333,	">$AC51":2297,	">$Heron_mitochondrion":2295.66666667,	">$clone_7":2298.625,	">$Waik37":2300.16666667,	">$Gunn":2292,	">$DenmarkA":2298.41666667,	">$Waik372":2294.16666667,	">$Tarawera":2298.16666667,	">$Poerua_triploid":2295.33333333,	">$Kaniere_triploid":2296.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2300.08333333,	">$Brunner_2_4n":2361.125,	">$Brunner_6_3n":2358.08333333,	">$Grasmere_1_4n":2594.33333333,	">$Grasmere_6_3n":2306.75,	">$Poerua_72_4n":2375.70833333,	">$Rotoiti_1_4n":2354.95833333,	">$*Kaniere_1_2n":2295.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2298,	">$*Yellow_Contig_56":2295.33333333,	">$*Alexsex":2295.33333333,	">$*AlexMap":2295.33333333,	">$*Lady":2297.33333333,	">$*Ianthe":2295.66666667,	">$*Rotoroa_1_2n":2343.83333333}
    C2Sites = {">$Duluth":5093.47916667,	">$Heron2":5090.33333333,	">$McGregor":5089.66666667,	">$Waik36":5100.75,	">$WalesC":5101.75,	">$clone_1":5091.33333333,	">$AC51":5089.33333333,	">$Heron_mitochondrion":5088.66666667,	">$clone_7":5092.14583333,	">$Waik37":5096.75,	">$Gunn":5090.33333333,	">$DenmarkA":5091.875,	">$Waik372":5097.41666667,	">$Tarawera":5097.08333333,	">$Poerua_triploid":5092,	">$Kaniere_triploid":5096.75,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5091.20833333,	">$Brunner_2_4n":5082.39583326,	">$Brunner_6_3n":5076.37499994,	">$Grasmere_1_4n":4999.33333297,	">$Grasmere_6_3n":5084.70833332,	">$Poerua_72_4n":5059.52083325,	">$Rotoiti_1_4n":5085.97916662,	">$*Kaniere_1_2n":5090,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5095.33333333,	">$*Yellow_Contig_56":5097.33333333,	">$*Alexsex":5097.33333333,	">$*AlexMap":5097.33333333,	">$*Lady":5089,	">$*Ianthe":5093,	">$*Rotoroa_1_2n":5078.41666662}
    R2Sites = {">$Duluth":3529,	">$Heron2":3525.66666667,	">$McGregor":3525.33333333,	">$Waik36":3526.33333333,	">$WalesC":3527.33333333,	">$clone_1":3524.66666667,	">$AC51":3526.33333333,	">$Heron_mitochondrion":3526.33333333,	">$clone_7":3529,	">$Waik37":3530.66666667,	">$Gunn":3526,	">$DenmarkA":3529,	">$Waik372":3527.33333333,	">$Tarawera":3530.33333333,	">$Poerua_triploid":3525,	">$Kaniere_triploid":3530.66666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3529,	">$Brunner_2_4n":3538,	">$Brunner_6_3n":3544.66666667,	">$Grasmere_1_4n":3586,	">$Grasmere_6_3n":3529.66666667,	">$Poerua_72_4n":3549,	">$Rotoiti_1_4n":3533.66666667,	">$*Kaniere_1_2n":3525.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3523.66666667,	">$*Yellow_Contig_56":3524.33333333,	">$*Alexsex":3524.33333333,	">$*AlexMap":3524.33333333,	">$*Lady":3526.33333333,	">$*Ianthe":3524,	">$*Rotoroa_1_2n":3537}
    C3Sites = {">$Duluth":2949.125,	">$Heron2":2945,	">$McGregor":2945,	">$Waik36":2947.16666667,	">$WalesC":2950.83333333,	">$clone_1":2944.66666667,	">$AC51":2945,	">$Heron_mitochondrion":2944.66666667,	">$clone_7":2949.79166667,	">$Waik37":2950.5,	">$Gunn":2944,	">$DenmarkA":2949.75,	">$Waik372":2952.83333333,	">$Tarawera":2950.5,	">$Poerua_triploid":2945.66666667,	">$Kaniere_triploid":2950.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2948.75,	">$Brunner_2_4n":2917.29166659,	">$Brunner_6_3n":2925.4166666,	">$Grasmere_1_4n":2832.33333297,	">$Grasmere_6_3n":2941.74999999,	">$Poerua_72_4n":2926.20833325,	">$Rotoiti_1_4n":2932.12499995,	">$*Kaniere_1_2n":2945.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2945.33333333,	">$*Yellow_Contig_56":2946.66666667,	">$*Alexsex":2946.66666667,	">$*AlexMap":2946.66666667,	">$*Lady":2947.33333333,	">$*Ianthe":2945.33333333,	">$*Rotoroa_1_2n":2928.16666662}
    R3Sites = {">$Duluth":5673.35416667,	">$Heron2":5671,	">$McGregor":5670,	">$Waik36":5679.91666667,	">$WalesC":5678.25,	">$clone_1":5671.33333333,	">$AC51":5670.66666667,	">$Heron_mitochondrion":5670.33333333,	">$clone_7":5671.35416667,	">$Waik37":5676.91666667,	">$Gunn":5672.33333333,	">$DenmarkA":5671.125,	">$Waik372":5671.91666667,	">$Tarawera":5676.91666667,	">$Poerua_triploid":5671.33333333,	">$Kaniere_triploid":5676.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5671.45833333,	">$Brunner_2_4n":5703.10416667,	">$Brunner_6_3n":5695.625,	">$Grasmere_1_4n":5753,	">$Grasmere_6_3n":5672.625,	">$Poerua_72_4n":5682.3125,	">$Rotoiti_1_4n":5687.52083333,	">$*Kaniere_1_2n":5670,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5673.66666667,	">$*Yellow_Contig_56":5675,	">$*Alexsex":5675,	">$*AlexMap":5675,	">$*Lady":5668,	">$*Ianthe":5671.66666667,	">$*Rotoroa_1_2n":5687.25}
    C4Sites = {">$Duluth":3422.02083333,	">$Heron2":3419.66666667,	">$McGregor":3420,	">$Waik36":3420.25,	">$WalesC":3423.25,	">$clone_1":3419.33333333,	">$AC51":3419,	">$Heron_mitochondrion":3419,	">$clone_7":3422.6875,	">$Waik37":3424.58333333,	">$Gunn":3420,	">$DenmarkA":3422.45833333,	">$Waik372":3428.25,	">$Tarawera":3424.91666667,	">$Poerua_triploid":3421,	">$Kaniere_triploid":3423.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3421.79166667,	">$Brunner_2_4n":3405.10416659,	">$Brunner_6_3n":3421.95833327,	">$Grasmere_1_4n":3382.99999963,	">$Grasmere_6_3n":3416.95833332,	">$Poerua_72_4n":3422.97916658,	">$Rotoiti_1_4n":3422.85416662,	">$*Kaniere_1_2n":3420.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3420,	">$*Yellow_Contig_56":3420.66666667,	">$*Alexsex":3420.66666667,	">$*AlexMap":3420.66666667,	">$*Lady":3423,	">$*Ianthe":3419.33333333,	">$*Rotoroa_1_2n":3414.91666662}
    R4Sites = {">$Duluth":5200.45833333,	">$Heron2":5196.33333333,	">$McGregor":5195,	">$Waik36":5206.83333333,	">$WalesC":5205.83333333,	">$clone_1":5196.66666667,	">$AC51":5196.66666667,	">$Heron_mitochondrion":5196,	">$clone_7":5198.45833333,	">$Waik37":5202.83333333,	">$Gunn":5196.33333333,	">$DenmarkA":5198.41666667,	">$Waik372":5196.5,	">$Tarawera":5202.5,	">$Poerua_triploid":5196,	">$Kaniere_triploid":5203.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5198.41666667,	">$Brunner_2_4n":5215.29166667,	">$Brunner_6_3n":5199.08333333,	">$Grasmere_1_4n":5202.33333333,	">$Grasmere_6_3n":5197.41666667,	">$Poerua_72_4n":5185.54166667,	">$Rotoiti_1_4n":5196.79166667,	">$*Kaniere_1_2n":5195.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5199,	">$*Yellow_Contig_56":5201,	">$*Alexsex":5201,	">$*AlexMap":5201,	">$*Lady":5192.33333333,	">$*Ianthe":5197.66666667,	">$*Rotoroa_1_2n":5200.5}
    C5Sites = {">$Duluth":4384.85416667,	">$Heron2":4382.33333333,	">$McGregor":4382,	">$Waik36":4383.58333333,	">$WalesC":4385.58333333,	">$clone_1":4382.33333333,	">$AC51":4382,	">$Heron_mitochondrion":4382.33333333,	">$clone_7":4385.1875,	">$Waik37":4385.58333333,	">$Gunn":4382.66666667,	">$DenmarkA":4385.125,	">$Waik372":4390.58333333,	">$Tarawera":4385.58333333,	">$Poerua_triploid":4383.33333333,	">$Kaniere_triploid":4386.25,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4383.79166667,	">$Brunner_2_4n":4338.9375,	">$Brunner_6_3n":4354.95833333,	">$Grasmere_1_4n":4238,	">$Grasmere_6_3n":4375.95833333,	">$Poerua_72_4n":4354.14583333,	">$Rotoiti_1_4n":4363.35416667,	">$*Kaniere_1_2n":4383.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4384,	">$*Yellow_Contig_56":4381.66666667,	">$*Alexsex":4381.66666667,	">$*AlexMap":4381.66666667,	">$*Lady":4385.33333333,	">$*Ianthe":4384.66666667,	">$*Rotoroa_1_2n":4354.91666667}
    R5Sites = {">$Duluth":4237.625,	">$Heron2":4233.66666667,	">$McGregor":4233,	">$Waik36":4243.5,	">$WalesC":4243.5,	">$clone_1":4233.66666667,	">$AC51":4233.66666667,	">$Heron_mitochondrion":4232.66666667,	">$clone_7":4235.95833333,	">$Waik37":4241.83333333,	">$Gunn":4233.66666667,	">$DenmarkA":4235.75,	">$Waik372":4234.16666667,	">$Tarawera":4241.83333333,	">$Poerua_triploid":4233.66666667,	">$Kaniere_triploid":4241.16666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4236.41666667,	">$Brunner_2_4n":4281.45833326,	">$Brunner_6_3n":4266.08333327,	">$Grasmere_1_4n":4347.33333297,	">$Grasmere_6_3n":4238.41666665,	">$Poerua_72_4n":4254.37499992,	">$Rotoiti_1_4n":4256.29166662,	">$*Kaniere_1_2n":4232.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4235,	">$*Yellow_Contig_56":4240,	">$*Alexsex":4240,	">$*AlexMap":4240,	">$*Lady":4230,	">$*Ianthe":4232.33333333,	">$*Rotoroa_1_2n":4260.49999996}
    C6Sites = {">$Duluth":4128.5625,	">$Heron2":4124.66666667,	">$McGregor":4124.33333333,	">$Waik36":4130.08333333,	">$WalesC":4129.75,	">$clone_1":4125.66666667,	">$AC51":4124.66666667,	">$Heron_mitochondrion":4125,	">$clone_7":4126.89583333,	">$Waik37":4123.41666667,	">$Gunn":4126.33333333,	">$DenmarkA":4127.04166667,	">$Waik372":4126.08333333,	">$Tarawera":4124.08333333,	">$Poerua_triploid":4126,	">$Kaniere_triploid":4125.75,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4126.04166667,	">$Brunner_2_4n":4078.47916674,	">$Brunner_6_3n":4075.2083334,	">$Grasmere_1_4n":3848.3333337,	">$Grasmere_6_3n":4112.54166668,	">$Poerua_72_4n":4050.43750008,	">$Rotoiti_1_4n":4084.39583338,	">$*Kaniere_1_2n":4126.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4125,	">$*Yellow_Contig_56":4127.33333333,	">$*Alexsex":4127.33333333,	">$*AlexMap":4127.33333333,	">$*Lady":4121,	">$*Ianthe":4123.66666667,	">$*Rotoroa_1_2n":4085.08333338}
    R6Sites = {">$Duluth":4493.91666667,	">$Heron2":4491.33333333,	">$McGregor":4490.66666667,	">$Waik36":4497,	">$WalesC":4499.33333333,	">$clone_1":4490.33333333,	">$AC51":4491,	">$Heron_mitochondrion":4490,	">$clone_7":4494.25,	">$Waik37":4504,	">$Gunn":4490,	">$DenmarkA":4493.83333333,	">$Waik372":4498.66666667,	">$Tarawera":4503.33333333,	">$Poerua_triploid":4491,	">$Kaniere_triploid":4501.66666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4494.16666667,	">$Brunner_2_4n":4541.91666674,	">$Brunner_6_3n":4545.8333334,	">$Grasmere_1_4n":4737.00000037,	">$Grasmere_6_3n":4501.83333335,	">$Poerua_72_4n":4558.08333342,	">$Rotoiti_1_4n":4535.25000005,	">$*Kaniere_1_2n":4489.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4494,	">$*Yellow_Contig_56":4494.33333333,	">$*Alexsex":4494.33333333,	">$*AlexMap":4494.33333333,	">$*Lady":4494.33333333,	">$*Ianthe":4493.33333333,	">$*Rotoroa_1_2n":4530.33333338}
    C7Sites = {">$Duluth":3873.77083333,	">$Heron2":3870.66666667,	">$McGregor":3870,	">$Waik36":3879.91666667,	">$WalesC":3880.58333333,	">$clone_1":3871.66666667,	">$AC51":3870.66666667,	">$Heron_mitochondrion":3870.33333333,	">$clone_7":3872.10416667,	">$Waik37":3874.25,	">$Gunn":3872.33333333,	">$DenmarkA":3871.625,	">$Waik372":3875.91666667,	">$Tarawera":3874.58333333,	">$Poerua_triploid":3872.66666667,	">$Kaniere_triploid":3875.91666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3870.29166667,	">$Brunner_2_4n":3832.85416667,	">$Brunner_6_3n":3825.79166667,	">$Grasmere_1_4n":3635.33333333,	">$Grasmere_6_3n":3860.45833333,	">$Poerua_72_4n":3801.89583333,	">$Rotoiti_1_4n":3832.9375,	">$*Kaniere_1_2n":3871.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3873.66666667,	">$*Yellow_Contig_56":3877,	">$*Alexsex":3877,	">$*AlexMap":3877,	">$*Lady":3869,	">$*Ianthe":3872.33333333,	">$*Rotoroa_1_2n":3832.58333333}
    R7Sites = {">$Duluth":4748.70833333,	">$Heron2":4745.33333333,	">$McGregor":4745,	">$Waik36":4747.16666667,	">$WalesC":4748.5,	">$clone_1":4744.33333333,	">$AC51":4745,	">$Heron_mitochondrion":4744.66666667,	">$clone_7":4749.04166667,	">$Waik37":4753.16666667,	">$Gunn":4744,	">$DenmarkA":4749.25,	">$Waik372":4748.83333333,	">$Tarawera":4752.83333333,	">$Poerua_triploid":4744.33333333,	">$Kaniere_triploid":4751.5,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4749.91666667,	">$Brunner_2_4n":4787.54166659,	">$Brunner_6_3n":4795.24999994,	">$Grasmere_1_4n":4949.99999963,	">$Grasmere_6_3n":4753.91666665,	">$Poerua_72_4n":4806.62499992,	">$Rotoiti_1_4n":4786.70833328,	">$*Kaniere_1_2n":4744,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4745.33333333,	">$*Yellow_Contig_56":4744.66666667,	">$*Alexsex":4744.66666667,	">$*AlexMap":4744.66666667,	">$*Lady":4746.33333333,	">$*Ianthe":4744.66666667,	">$*Rotoroa_1_2n":4782.83333329}
    meanCSites = {">$Duluth":4310.80952381,	">$Heron2":4307.57142857143,	">$McGregor":4307.14285714286,	">$Waik36":4313.14285714286,	">$WalesC":4314.99999999857,	">$clone_1":4307.80952381,	">$AC51":4307.04761904857,	">$Heron_mitochondrion":4307.04761904714,	">$clone_7":4310.19047619,	">$Waik37":4311.76190476143,	">$Gunn":4308.57142857,	">$DenmarkA":4310.04761904714,	">$Waik372":4314.52380952286,	">$Tarawera":4312.28571428429,	">$Poerua_triploid":4308.90476190571,	">$Kaniere_triploid":4312.80952380857,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4308.85714285857,	">$Brunner_2_4n":4273.47619044429,	">$Brunner_6_3n":4277.52380949714,	">$Grasmere_1_4n":4132.47619031857,	">$Grasmere_6_3n":4299.99999999429,	">$Poerua_72_4n":4263.99999996286,	">$Rotoiti_1_4n":4283.76190474143,	">$*Kaniere_1_2n":4308.23809523714,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4309.19047619,	">$*Yellow_Contig_56":4311,	">$*Alexsex":4311,	">$*AlexMap":4311,	">$*Lady":4307.52380952286,	">$*Ianthe":4308.52380952286,	">$*Rotoroa_1_2n":4280.80952379}
    meanRSites = {">$Duluth":4311.66964285714,	">$Heron2":4308.42857142857,	">$McGregor":4307.85714285714,	">$Waik36":4313.94047619,	">$WalesC":4314.08333333143,	">$clone_1":4308.19047619,	">$AC51":4308.61904762,	">$Heron_mitochondrion":4307.95238095286,	">$clone_7":4310.95535714286,	">$Waik37":4315.65476190571,	">$Gunn":4307.76190476143,	">$DenmarkA":4310.82738095286,	">$Waik372":4310.22619047714,	">$Tarawera":4315.13095238,	">$Poerua_triploid":4308.09523809429,	">$Kaniere_triploid":4314.60714285714,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4311.35119047714,	">$Brunner_2_4n":4346.91964284714,	">$Brunner_6_3n":4343.51785713429,	">$Grasmere_1_4n":4452.85714280429,	">$Grasmere_6_3n":4314.37499999857,	">$Poerua_72_4n":4344.52083332286,	">$Rotoiti_1_4n":4335.88392856429,	">$*Kaniere_1_2n":4307.42857142714,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4309.80952381,	">$*Yellow_Contig_56":4310.66666666571,	">$*Alexsex":4310.66666666571,	">$*AlexMap":4310.66666666571,	">$*Lady":4307.80952380714,	">$*Ianthe":4308.47619047714,	">$*Rotoroa_1_2n":4334.60714285143}
    logfile = open(fasta[0:-5] + '_singletons.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
    refSeq = seqDict[popList[0]]
    synDict = {}
    meanCDict = {}
    meanRDict = {}
    C1Dict = {}
    R1Dict = {}
    C2Dict = {}
    R2Dict = {}
    C3Dict = {}
    R3Dict = {}
    C4Dict = {}
    R4Dict = {}
    C5Dict = {}
    R5Dict = {}
    C6Dict = {}
    R6Dict = {}
    C7Dict = {}
    R7Dict = {}
    for site in range(len(refSeq)):
        codonNum = site/3
        pos = (site+1)%3
        if pos == 1:
            nucPos = 1
        elif pos == 2:
            nucPos = 2
        elif pos == 0:
            nucPos = 3
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if site >= start and site <= stop:
                gene = positionDict[locus]
                geneStart = locus[0]
                if site == geneStart or site == (geneStart+1) or site == (geneStart + 2):
                    startCodon = True
                else:
                    startCodon = False
        currAlleleDict = {}
        currAlleleList = []
        currCodonDict = {}
        currCodonList = []
        allele2CodonTable = {}
        for seq in popList:
            if seq not in synDict:
                synDict[seq] = 0
                meanCDict[seq] = 0
                meanRDict[seq] = 0
                C1Dict[seq] = 0
                R1Dict[seq] = 0
                C2Dict[seq] = 0
                R2Dict[seq] = 0
                C3Dict[seq] = 0
                R3Dict[seq] = 0
                C4Dict[seq] = 0
                R4Dict[seq] = 0
                C5Dict[seq] = 0
                R5Dict[seq] = 0
                C6Dict[seq] = 0
                R6Dict[seq] = 0
                C7Dict[seq] = 0
                R7Dict[seq] = 0
            currSeq = seqDict[seq]
            currCodons = codonDict[seq]
            currNuc = currSeq[site]
            currCodon = currCodons[codonNum]
            allele2CodonTable[currNuc] = currCodon
            if currCodon not in currCodonList and 'N' not in currCodon and '-' not in currCodon:
                currCodonDict[currCodon] = [seq]
                currCodonList.append(currCodon)
                if currNuc not in currAlleleList:
                    currAlleleList.append(currNuc)
                    currAlleleDict[currNuc] = [seq]
                else:
                    currList = currAlleleDict[currNuc]
                    currList.append(seq)
                    currAlleleDict[currNuc] = currList
            elif 'N' not in currCodon and '-' not in currCodon:
                currCodonSeqList = currCodonDict[currCodon]
                currCodonSeqList.append(seq)
                currCodonDict[currCodon] = currCodonSeqList
                currList = currAlleleDict[currNuc]
                currList.append(seq)
                currAlleleDict[currNuc] = currList
        if len(currAlleleDict) > 1:
            singletonList = []
            currAAList = []
            for allele in currAlleleList:
                if len(currAlleleDict[allele]) == 1:
                    singletonList.append(allele)
            if len(singletonList) > 0 and len(currCodonDict) == 2:
                if startCodon == True:
                    if currCodonList[0] in startCodons:
                        currAAList.append('M')
                    else:
                        currAAList.append(geneticCode[currCodonList[0]])
                    if currCodonList[1] not in startCodons and geneticCode[currCodonList[1]] not in currAAList:
                        currAAList.append(geneticCode[currCodonList[1]])
                    elif geneticCode[currCodonList[1]] not in currAAList:
                        currAAList.append('M')
                else:
                    currAAList.append(geneticCode[currCodonList[0]])
                    if geneticCode[currCodonList[1]] not in currAAList:
                        currAAList.append(geneticCode[currCodonList[1]])
                if len(currAAList) == 1:
                    currLineage = currAlleleDict[singletonList[0]]
                    synDict[currLineage[0]] += 1
                else:
                    currLineage = currAlleleDict[singletonList[0]]
                    mutType = CRI(currAAList)
                    if mutType[0] == 0:
                        C1Dict[currLineage[0]] += 1
                    else:
                        R1Dict[currLineage[0]] += 1
                    if mutType[1] == 0:
                        C2Dict[currLineage[0]] += 1
                    else:
                        R2Dict[currLineage[0]] += 1
                    if mutType[2] == 0:
                        C3Dict[currLineage[0]] += 1
                    else:
                        R3Dict[currLineage[0]] += 1
                    if mutType[3] == 0:
                        C4Dict[currLineage[0]] += 1
                    else:
                        R4Dict[currLineage[0]] += 1
                    if mutType[4] == 0:
                        C5Dict[currLineage[0]] += 1
                    else:
                        R5Dict[currLineage[0]] += 1
                    if mutType[5] == 0:
                        C6Dict[currLineage[0]] += 1
                    else:
                        R6Dict[currLineage[0]] += 1
                    if mutType[6] == 0:
                        C7Dict[currLineage[0]] += 1
                    else:
                        R7Dict[currLineage[0]] += 1
                    if mutType[7] <= 0.5:
                        meanCDict[currLineage[0]] += 1
                    else:
                        meanRDict[currLineage[0]] += 1
            elif len(singletonList) > 0:
                logfile.write(str(site+1) + '\t' + str(nucPos) + '\t' + str(codonNum +1) + '\n')
    sys.stdout.write('Lineage\t#Syn Private Alleles\t# Syn Sites\t# meanC Private Alleles\t# meanC Sites\t# meanR Private Alleles\t# meanR Sites\t# C1 Private Alleles\t# C1 Sites\t# R1 Private Alleles\t# R1 Sites\t# C2 Private Alleles\t# C2 Sites\t# R2 Private Alleles\t# R2 Sites\t# C3 Private Alleles\t# C3 Sites\t# R3 Private Alleles\t# R3 Sites\t# C4 Private Alleles\t# C4 Sites\t# R4 Private Alleles\t# R4 Sites\t# C5 Private Alleles\t# C5 Sites\t# R5 Private Alleles\t# R5 Sites\t# C6 Private Alleles\t# C6 Sites\t# R6 Private Alleles\t# R6 Sites\t# C7 Private Alleles\t# C7 Sites\t# R7 Private Alleles\t# R7 Sites\n')
    for lineage in popList:
        sys.stdout.write(lineage + '\t' + str(synDict[lineage]) + '\t' + str(synSites[lineage]) + '\t' + str(meanCDict[lineage]) + '\t' + str(meanCSites[lineage]) + '\t' + str(meanRDict[lineage]) + '\t' + str(meanRSites[lineage]) + '\t' + str(C1Dict[lineage]) + '\t' + str(C1Sites[lineage]) + '\t' + str(R1Dict[lineage]) + '\t' + str(R1Sites[lineage]) + '\t' + str(C2Dict[lineage]) + '\t' + str(C2Sites[lineage]) + '\t' + str(R2Dict[lineage]) + '\t' + str(R2Sites[lineage]) + '\t' + str(C3Dict[lineage]) + '\t' + str(C3Sites[lineage]) + '\t' + str(R3Dict[lineage]) + '\t' + str(R3Sites[lineage]) + '\t' + str(C4Dict[lineage]) + '\t' + str(C4Sites[lineage]) + '\t' + str(R4Dict[lineage]) + '\t' + str(R4Sites[lineage]) + '\t' + str(C5Dict[lineage]) + '\t' + str(C5Sites[lineage]) + '\t' + str(R5Dict[lineage]) + '\t' + str(R5Sites[lineage]) + '\t' + str(C6Dict[lineage]) + '\t' + str(C6Sites[lineage]) + '\t' + str(R6Dict[lineage]) + '\t' + str(R6Sites[lineage]) + '\t' + str(C7Dict[lineage]) + '\t' + str(C7Sites[lineage]) + '\t' + str(R7Dict[lineage]) + '\t' + str(R7Sites[lineage]) + '\n')
    
                
    
    

            
        
        
    
    

#polSub(sys.argv[1])