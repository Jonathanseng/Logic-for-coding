def banach_tarski(ball):
    points = ball.points
    half_points = []
    for point in points:
        half_points.append((point[0] / 2, point[1] / 2))
        half_points.append((point[0] / 2, -point[1] / 2))
        half_points.append((-point[0] / 2, point[1] / 2))
        half_points.append((-point[0] / 2, -point[1] / 2))
    return ball.copy(points=half_points), ball.copy(points=points)


def main():
    ball = Ball(origin=(0, 0), radius=1)
    new_balls = banach_tarski(ball)
    print(new_balls[0].volume)
    print(new_balls[1].volume)


if __name__ == "__main__":
    main()
