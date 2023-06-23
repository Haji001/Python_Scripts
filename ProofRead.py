import lmproof 

def ProofRead(text):

    ProofRead = lmproof.load('en')
    Correction = ProofRead.proofread(text)

    print(f"The Original Text: {text}")
    print(" ")
    print(f"The Correction: {Correction}")

ProofRead("While working, many devs love listening to music.")