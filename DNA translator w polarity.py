dnaSequence = input("Enter dna sequence: uaagugauauaguagua")
dnaSequence = dnaSequence.upper()

polypetideChain = ""
abbreviatedChain = ""
polar = 0
nonpolar = 0
chargeChain = ""

for i in range(len(dnaSequence)):
    if dnaSequence[i] == "A" or dnaSequence[i] == "G" or dnaSequence[i] == "C" or dnaSequence[i] == "U":
        continue
    else:
        print("Make sure to only use the initials a, c, u, and g")
        exit()

if len(dnaSequence) % 3 == 0:
    print("You have", len(dnaSequence)/3, "amino acids in your sequence")
else: 
    print("You do not have a chain that is divisible by 3, you only have", len(dnaSequence), "nucleic acids")
    exit()

codons = {
    "UUU" : ["Phenylalinine", "F", "nonpolar"],
    "UUC" : ["Phenylalinine", "F", "nonpolar"],
    "UUA" : ["Leucine", "L", "nonpolar"],
    "UUG" : ["Leucine", "L", "nonpolar"],
    "CUU" : ["Leucine", "L", "nonpolar"],
    "CUC" : ["Leucine", "L", "nonpolar"],
    "CUA" : ["Leucine", "L", "nonpolar"],
    "CUG" : ["Leucine", "L", "nonpolar"],
    "AUU" : ["Isoleucine", "I", "nonpolar"],
    "AUC" : ["Isoleucine", "I", "nonpolar"],
    "AUA" : ["Isoleucine", "I", "nonpolar"],
    "AUG" : ["Methionine", "M", "nonpolar"],
    "GUU" : ["Valine", "V", "nonpolar"],
    "GUC" : ["Valine", "V", "nonpolar"],
    "GUA" : ["Valine", "V", "nonpolar"],
    "GUG" : ["Valine", "V", "nonpolar"],
    "UCU" : ["Serine", "S", "uncharged polar"],
    "UCC" : ["Serine", "S", "uncharged polar"],
    "UCA" : ["Serine", "S", "uncharged polar"],
    "UCG" : ["Serine", "S", "uncharged polar"],
    "CCU" : ["Proline", "P", "nonpolar"],
    "CCC" : ["Proline", "P", "nonpolar"],
    "CCA" : ["Proline", "P", "nonpolar"],
    "CCG" : ["Proline", "P", "nonpolar"],
    "ACU" : ["Threonine" , "T", "uncharged polar"],
    "ACC" : ["Threonine" , "T", "uncharged polar"],
    "ACA" : ["Threonine" , "T", "uncharged polar"],
    "ACG" : ["Threonine" , "T", "uncharged polar"],
    "GCU" : ["Alanine" , "A", "nonpolar"],
    "GCC" : ["Alanine" , "A", "nonpolar"],
    "GCA" : ["Alanine" , "A", "nonpolar"],
    "GCG" : ["Alanine" , "A", "nonpolar"],
    "UAU" : ["Tyrosine" , "Y", "uncharged polar"],
    "UAC" : ["Tyrosine" , "Y", "uncharged polar"],
    "UAG" : ["and then a break", " ", ""],
    "UAA" : ["and then a break", " ", ""],
    "UGA" : ["and then a break", " ", ""],
    "CAU" : ["Histidine", "H", "positive"],
    "CAC" : ["Histidine", "H", "positive"],
    "CAA" : ["Glutamine", "Q", "uncharged polar"],
    "CAG" : ["Glutamine", "Q", "uncharged polar"],
    "AAA" : ["Lysine", "L", "positive"],
    "AAG" : ["Lysine", "L", "positive"],
    "GAU" : ["Aspartic Acid", "D", "negative"],
    "GAC" : ["Aspartic Acid", "D", "negative"],
    "GAA" : ["Glutamic Acid", "E", "negative"],
    "GAG" : ["Glutamic Acid", "E", "negative"],
    "UGU" : ["Cysteine", "C", "nonpolar"],
    "UGC" : ["Cysteine", "C", "nonpolar"],
    "UGG" : ["Tryptophan", "W", "nonpolar"],
    "CGU" : ["Arginine", "R", "positive"],
    "CGC" : ["Arginine", "R", "positive"],
    "CGA" : ["Arginine", "R", "positive"],
    "CGG" : ["Arginine", "R", "positive"],
    "AGA" : ["Arginine", "R", "positive"],
    "AGG" : ["Arginine", "R", "positive"],
    "AGU" : ["Serine", "S", "nonpolar"],
    "AGC" : ["Serine", "S", "nonpolar"],
    "GGU" : ["Glycine", "G", "nonpolar"],
    "GGC" : ["Glycine", "G", "nonpolar"],
    "GGA" : ["Glycine", "G", "nonpolar"],
    "GGG" : ["Glycine", "G", "nonpolar"],
}

numberOfAminoAcids = len(dnaSequence) / 3

for i in range(int(numberOfAminoAcids)):
    codon = codons[dnaSequence[(3*i):(3*(i + 1))]]
    polypetideChain = polypetideChain + codon[0] + ", "
    abbreviatedChain = abbreviatedChain + codon[1]
    if codon[2] == "nonpolar": 
        nonpolar = nonpolar + 1
        chargeChain = chargeChain + " "
    elif codon[2] == "negative" :
        polar = polar + 1
        chargeChain = chargeChain + "-"
    elif codon[2] == "positive" :
        polar = polar + 1
        chargeChain = chargeChain + "+"
    elif codon[2] == "uncharged polar" :
        polar = polar + 1
        chargeChain = chargeChain + "*"
    else:
        chargeChain = chargeChain + " "

print("The polypedtide chain is: ", polypetideChain)
print("The abbreviated chain is: ", abbreviatedChain)
print("The charges in order are: ", chargeChain)

if (numberOfAminoAcids*(2/3)) >= nonpolar > (numberOfAminoAcids/2) :
    print("It is slightly nonpolar")
elif nonpolar > (numberOfAminoAcids*(2/3)) :
    print("It is mostly nonpolar")
elif (numberOfAminoAcids*(2/3)) >= polar > (numberOfAminoAcids/2) :
    print("It is slightly polar")
elif polar > (numberOfAminoAcids*(2/3)) :
    print("it is mostly polar")
else:
    print("It is perfectly amphipathic")
