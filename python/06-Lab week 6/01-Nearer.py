"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice = int(input())
    dis_alice = abs(alice-ice)
    dis_bob = abs(bob-ice)
    if dis_alice > dis_bob:
        print(f"Bob {dis_bob}")
    elif dis_alice < dis_bob:
        print(f"Alice {dis_alice}")
    elif dis_alice == dis_bob:
        print(f"Sundaes {dis_bob}")
main()
