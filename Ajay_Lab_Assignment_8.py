def max_Production():
    i,y,R,S = get_Relation()
    RoS = [ max([ i*j for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in R for col in S]
    RoS = np.array(RoS).reshape((i,y))
    print("max-production Composition\n",RoS)
    return RoS

def max_min():
    i,y,R,S = get_Relation()
    R_S = [ max([ min(i,j) for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in R for col in S]
    R_S = np.array(R_S).reshape((i,y))
    print("min-max Composition\n",R_S)
    return R_S

