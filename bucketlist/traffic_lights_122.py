import sys

def calc_time(d, L):
    pass
    t_elapsed = 0
    d_driven = 0
    for light in L:
        t_elapsed += light[0] - d_driven
        d_driven = light[0]
        wait = det_state_of_light(t_elapsed, light)
        t_elapsed += wait
    t_elapsed += d - d_driven
    return t_elapsed
def det_state_of_light(t, light):
    r_l = light[1]
    g_l = light[2]
    temp = t % (r_l + g_l)
    return r_l - temp if r_l - temp > 0 else 0
def main():
    d = sys.stdin
    L = []
    total_length = int(d.readline().strip())
    for i in d:
        i = i.strip()
        L.append([int(e) for e in i.split()])
    #print(total_length, L)
    print(calc_time(total_length, L))
if __name__ == '__main__':
    main()
