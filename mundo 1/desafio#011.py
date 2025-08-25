larg = float(input('qual a largura da parade?'))
alt = float(input('qual a altura da parade?'))
area = larg*alt
print('sua parade tem dimensão de {}x{} e sua area tem {}m² '.format(larg,alt,area))
tinta = area/2
print('para pintar essa parade, voce vai precisar {}L'.format(tinta))