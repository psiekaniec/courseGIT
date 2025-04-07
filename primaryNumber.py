import math

if __name__ == "__main__":
    n = []
    output_list = []
    constraint_max = 2000000001
    input_max = 31
    t = int(input())
    if t in range(1, input_max):
        for i in range(t):
            inp = int(input())
            if inp in range (1, constraint_max):
                n.append(inp)
        
        for e in n:
            prime = "Prime"
            if e < 2:
                prime = "Not prime"
            else:
                for i in range(2, int(math.sqrt(e)) + 1):
                    if e % i == 0:
                        prime = "Not prime"
            output_list.append(prime)
        
    for i in output_list:
        print(i)