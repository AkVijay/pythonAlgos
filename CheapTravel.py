if __name__ == '__main__':
    data = [int(m) for m in input().split()]
    cost_single_rides =  data[0] * data[2]
    cost_multiple_rides = data[3] if data[1] >= data[0] else min(data[0]//data[1] * data[3] + data[0]%data[1] * data[2],
                                                                 (data[0]//data[1] + 1) * data[3])
    print(min(cost_single_rides, cost_multiple_rides))

