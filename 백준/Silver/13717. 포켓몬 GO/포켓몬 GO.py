def evolve_pokemon(N, pokemon_data):
    total_evolved = 0
    max_evolved = 0
    max_evolved_pokemon = ""

    for name, K, M in pokemon_data:
        evolved = 0
        while M >= K:
            M = M - K + 2
            evolved += 1
        total_evolved += evolved
        if evolved > max_evolved:
            max_evolved = evolved
            max_evolved_pokemon = name

    return total_evolved, max_evolved_pokemon

N = int(input())
pokemon_data = []
for _ in range(N):
    name = input()
    K, M = map(int, input().split())
    pokemon_data.append((name, K, M))

total_evolved, max_evolved_pokemon = evolve_pokemon(N, pokemon_data)
print(total_evolved)
print(max_evolved_pokemon)
