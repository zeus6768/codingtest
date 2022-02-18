from itertools import permutations, combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

possible_teams = list(combinations(range(0, N), N//2))

def make_link_team(N:int, start_team:list) -> tuple:
	population = list(range(N))
	[population.remove(num) for num in start_team]
	link_team = tuple(population)
	return link_team

def team_ability(team:tuple, S:list) -> int:
	sum_ability = 0
	for p0, p1 in list(permutations(team, 2)):
		sum_ability += S[p0][p1]
	return sum_ability

def result(N:int, possible_teams:list, S:list) -> int:
	ability_gap = []
	for start_team in possible_teams:
		link_team = make_link_team(N, start_team)
		start_ability = team_ability(start_team, S)
		link_ability = team_ability(link_team, S)
		gap = abs(start_ability - link_ability)
		ability_gap.append(gap)
	return min(ability_gap)

answer = result(N, possible_teams, S)
print(answer)

## 같지만 다른 풀이
ability_gap = []
for start_team in possible_teams:
	population = list(range(N))
	[population.remove(num) for num in start_team]
	link_team = population
	start_ability = 0
	link_ability = 0
	for p0, p1 in list(permutations(start_team, 2)):
		start_ability += S[p0][p1]
	for p0, p1 in list(permutations(link_team, 2)):
		link_ability += S[p0][p1]
	gap = abs(start_ability - link_ability)
	ability_gap.append(gap)
	
print(min(ability_gap))