from pyscf import gto, scf

mol = gto.Mole()
mol.atom = 'O 0 0 0; H 0 0 1; H 0 1 0'
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
print("SCF energy:", mf.kernel())