class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set=set(map(tuple,obstacles))

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0

        x=y=0
        max_distance=0

        for cmd in commands:
            if cmd==-1:
                d=(d+1)%4
            elif cmd==-2:
                d=(d-1)%4
            else:
                dx,dy=dirs[d]
            
            for _  in range (cmd):
                nx=x+dx
                ny=y+dy

                if (nx,ny) in obstacle_set:
                    break
                
                x,y=nx,ny
                max_distance=max(max_distance,x ** 2 + y **2)
    
        return max_distance