'''
blob = {colors:[R,G,B]}
'''

class attract (object):
    '''defines how attracted a blob is to other blobs'''

    def __init__ (self, blob):
        R = 0; G = 1; B = 2
        self.blob = blob
        R_ideal = ideal_R(self.blob(colors(R)))
        G_ideal = ideal_R(self.blob(colors(G)))
        B_ideal = ideal_R(self.blob(colors(R,G,B)))
        self.ideals(R_ideal, G_ideal, B_ideal)

    def ideal_R (self, R):
        '''
        Red is het, attraction to colors that are different from you
        The less red you are, the more you are attracted to red
        sky blues (0,255,255) are most attracted to reds (255,0,0)
        '''
        return (-R+255)

    def ideal_G (self, G):
        '''
        Gay is gay, attraction to colors like yourself
        The more green you are, the more you are attracted to green
        greens (0,255,0) are most attracted to greens (0,255,0)
        '''
        return (G)

    def ideal_B (self, R, G, B):
        '''
        Blue is pansexuality, attraction to all colors
        The more color you have, the more you are attracted to blue
        blacks (255,255,255) are most attracted to blues (0,0,255)
        '''
        return ((R+G+B)/(3))

    #WIP
    def attraction (self, other):
        R = 0; G = 1; B = 2
