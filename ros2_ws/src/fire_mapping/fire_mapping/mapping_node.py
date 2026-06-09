import rclpy
from rclpy.node import Node


class MappingNode(Node):

    def __init__(self):

        super().__init__('mapping_node')

        self.get_logger().info("Fire Mapping Node Started")

        self.map_width = 20
        self.map_height = 20

        # Robot start position
        self.robot_x = 10
        self.robot_y = 10

        # Fires: (x, y, intensity)
        # 2 = Small
        # 3 = Medium
        # 4 = Large
        self.fires = [
            (3, 3, 2),
            (7, 15, 3),
            (15, 5, 4)
        ]

        # Choose highest priority fire
        self.target_fire = max(
            self.fires,
            key=lambda fire: fire[2]
        )

        self.fire_x = self.target_fire[0]
        self.fire_y = self.target_fire[1]

        self.get_logger().info(
            f"Target selected: Fire at ({self.fire_x}, {self.fire_y}) "
            f"Intensity={self.target_fire[2]}"
        )

        self.timer = self.create_timer(
            5.0,
            self.timer_callback
        )

    def timer_callback(self):

        # Stop if target reached
        if (
            self.robot_x == self.fire_x and
            self.robot_y == self.fire_y
        ):
            print("\n🚒 TARGET FIRE REACHED! 🚒")
            return

        # Fresh map
        self.grid = [
            [0 for _ in range(self.map_width)]
            for _ in range(self.map_height)
        ]

        # Obstacles
        self.grid[8][8] = 1
        self.grid[8][9] = 1
        self.grid[9][8] = 1

        # Move robot toward selected fire
        if self.robot_x < self.fire_x:
            self.robot_x += 1
        elif self.robot_x > self.fire_x:
            self.robot_x -= 1

        if self.robot_y < self.fire_y:
            self.robot_y += 1
        elif self.robot_y > self.fire_y:
            self.robot_y -= 1

        # Place fires
        for fire in self.fires:

            x = fire[0]
            y = fire[1]
            intensity = fire[2]

            self.grid[y][x] = intensity

        # Place robot
        self.grid[self.robot_y][self.robot_x] = 5

        print("\n===== FIRE PRIORITY MAP =====")

        for row in self.grid:

            line = ""

            for cell in row:

                if cell == 0:
                    line += ". "

                elif cell == 1:
                    line += "X "

                elif cell == 2:
                    line += "s "

                elif cell == 3:
                    line += "m "

                elif cell == 4:
                    line += "L "

                elif cell == 5:
                    line += "R "

            print(line)

        print("============================")


def main(args=None):

    rclpy.init(args=args)

    node = MappingNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
