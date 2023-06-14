import streamlit as st
import pandas as pd


def DNA_nucleotide_count(seq):
    """
    Counts the number of occurrences of each nucleotide in a DNA sequence.

    Parameters:
        seq: The DNA sequence.

    Returns:
        A dictionary that maps each nucleotide to its count.
    """

    d = {}
    for nucleotide in "ACGT":
        d[nucleotide] = seq.count(nucleotide)

    return d


def main():
    """The main function."""

    st.write("""
    # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of query DNA!

    ***
    """)

    sequence_input = '>DNAQuery\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGA'

    # Get the DNA sequence from the user.
    sequence = st.text_area("DNA Sequence", value=sequence_input, height=250)
    sequence = ''.join(sequence.splitlines()[1:])

    # Count the nucleotides in the DNA sequence.
    nucleotides = DNA_nucleotide_count(sequence)

    st.write('***')

    st.header('INPUT (DNA Query)')
    st.write(sequence)

    st.write('***')
    st.header('OUTPUT (DNA Nucleotide Count)')

    # Display the results.
    # 1. Print dictionary
    st.subheader('1. Print dictionary')
    nucleotides 

    # 2. Print text
    st.subheader('2. Print text')
    st.write(f"There are {nucleotides['A']} adenine (A)")
    st.write(f"There are {nucleotides['T']} thymine (T)")
    st.write(f"There are {nucleotides['G']} guanine (G)")
    st.write(f"There are {nucleotides['C']} cytosine (C)")

    # 3. Display DataFrame
    st.subheader('3. Display DataFrame')
    df = pd.DataFrame.from_dict(nucleotides, orient="index")
    df.reset_index(inplace=True)
    df = df.rename({0: "count", "index": "nucleotide"}, axis="columns")
    st.write(df)

    # 4. Display Bar chart
    st.subheader('4. Display Bar chart')
    st.bar_chart(df.groupby("nucleotide").sum())


if __name__ == "__main__":
    main()


# import streamlit as st
# import pandas as pd

# st.write("""
# # DNA Nucleotide Count Web App

# This app counts the nucleotide composition of query DNA!

# ***
# """)


# st.header('Ender DNA sequence')

# sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCT"

# sequence = st.text_area('Sequence input', sequence_input, height=250)
# sequence = sequence.splitlines()
# sequence = sequence[1:]
# sequence = ''.join(sequence)

# st.write('***')

# st.header('INPUT (DNA Query)')
# sequence

# st.header('OUTPUT (DNA Nucleotide Count)')

# # 1. print dictionary
# st.subheader('1. Print dictionary') 
# def DNA_nucleotide_count(seq):
#     d = dict([
#         ('A', seq.count('A')),
#         ('T', seq.count('T')),
#         ('G', seq.count('G')),
#         ('C', seq.count('C')),
#     ])

#     return d

# X = DNA_nucleotide_count(sequence)
# X_label = list(X)
# X_values = list(X.values())

# X

# # 2. Print text
# st.subheader('2. Print text')
# st.write(f'There are {X["A"]} adenine (A)')
# st.write(f'There are {X["T"]} thymine (T)')
# st.write(f'There are {X["G"]} guanine (G)')
# st.write(f'There are {X["C"]} cytosine (C)')

# # 3. Display DataFrame
# st.subheader('3. Display DataFrame')
# df = pd.DataFrame.from_dict(X, orient='index')
# df.reset_index(inplace=True)
# df = df.rename({0: 'count', 'index': 'nucleotide'}, axis='columns')
# st.write(df)

# # 4. Display Bar Chart
# st.subheader('4. Display Bar chart')
# st.bar_chart(df.groupby('nucleotide').sum())



