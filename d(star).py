import heapq

graf = {                        # Graf veri yapısı
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 1, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 4},
    'E': {'D': 4}
}



def dStar(graf, baslangıc):                                 #D* algoritması
    distances = {vertex: float('inf') for vertex in graf}
    distances[baslangıc] = 0
    pq = [(0, baslangıc)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graf[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


distances = dStar(graf, 'A')
print("Girilen Noktanın diğer düğümlere uzaklığı: ",distances)
