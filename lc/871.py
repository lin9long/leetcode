import heapq


class Soluation:

    def minPath(self, target, startFuel, stations):
        n_l = []

        if len(stations) == 0 and startFuel < target:
            return -1

        stations = [[0, startFuel]] + stations

        for i, j in stations[1:]:
            heapq.heappush(n_l, (i + j, i))

        count = 0
        start = 0
        fuel = startFuel
        while start + fuel < target and n_l:
            for p in range(len(n_l)):
                item = heapq.nlargest(p + 1, n_l)
                print(item)
                total, path = item[p][0], item[p][1]
                if path <= start + fuel:
                    if total >= target:
                        count += 1
                        return count
                    print('total = ', total, 'path = ', path, 'start = ', start, 'fule = ', fuel, 'count = ', count)
                    fuel = path - start - fuel + total - path
                    start = path
                    count += 1
                    n_l.remove(item[-1])
                    break
                elif p == len(n_l) - 1:
                    return -1
        return count


if __name__ == '__main__':
    # 100
    # 25
    # [[25, 25], [50, 25], [75, 25]]

    s = Soluation()
    res = s.minPath(target=100, startFuel=50, stations=[[25,50],[50,25]])
    # [[10, 60], [20, 30], [30, 30], [60, 40]]
    # [[25, 25], [50, 25], [75, 25]]
    print(res)
