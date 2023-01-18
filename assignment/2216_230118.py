s_triangle_sides = sorted(list(map(int ,input().split())))
answer = "삼각형"

first_side = s_triangle_sides[0]
second_side = s_triangle_sides[1]
thrid_side = s_triangle_sides[2]

if first_side == thrid_side:
    answer = "정삼각형"
elif first_side == second_side or second_side == thrid_side:
    answer = "이등변삼각형"
elif first_side**2 + second_side**2 == thrid_side**2:
    answer = "직각삼각형"

if first_side + second_side > thrid_side:
    answer = "삼각형 아님"

print(answer)