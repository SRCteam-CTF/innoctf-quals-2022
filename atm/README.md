# Armenian ATM writeup

Given: (atm)[atm]

The goal of this reverse task was to understand the c++ source code. We need to bypass `Dispenser` boolean flag check and password check. To bypass boolean flag check we need to pull all banknotes from the dispenser and push them back. To bypass password check we need to generate the same password using the same [generator](atm.cpp) as in `ATM::ATM` that is based on `srand(time(0))`, so it's simple to attack generator.

[solution script](atm.py)

Flag: `Ararat{cAlM_D0wn_4nd_T4ke_yOur_mOney}`