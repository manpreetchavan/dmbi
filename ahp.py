prop_mat = [[1,3,2],[0.33,1,0.2],[0.5,5,1]]
dist_mat = [[1,6,0.33],[0.166,1,0.11],[3,9,1]]
cost_mat = [[1,0.33,1],[3,1,9],[1,0.11,1]]
qual_mat = [[1,0.33,0.5],[3,1,4],[2,0.25,1]]

def property():
    sum_prop = [0,0,0]
    col_sum=[0,0,0]
    for i in range(0,3):
        for j in range(0,3):
            print(i,j)
            col_sum[i]=col_sum[i] + prop[j][i]
            # print(prop[j][i])

    # print(prop)
    for i in range(0,3):
        for j in range(0,3):
            prop[j][i]=prop[j][i]/col_sum[i]
    
    for i in range(0,3):
        for j in range(0,3):
            sum_prop[i]=sum_prop[i]+prop[i][j]
        

    print("\n",col_sum)
    print(sum_prop)
    print(prop)


def priority(prop):
    row_sum = [0,0,0]
    col_sum=[0,0,0]
    for i in range(0,3):
        for j in range(0,3):
            # print(i,j)
            col_sum[i]=col_sum[i] + prop[j][i]
            # print(prop[j][i])

    print(prop)
    
    for i in range(0,3):
        for j in range(0,3):
            prop[j][i]=prop[j][i]/col_sum[i]
    
    for i in range(0,3):
        for j in range(0,3):
            row_sum[i]=row_sum[i]+prop[i][j]
        row_sum[i]=row_sum[i]/3
        

    print(col_sum)
    print(row_sum)
    # print(prop)


priority(prop_mat)
print("\n")
print("----------------------")
priority(dist_mat)
print("\n----------------------\n")
priority(cost_mat)
print("\n----------------------\n")
priority(qual_mat)
