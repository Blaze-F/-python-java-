def solution(wallpaper):
    
    #시작점 x,y 표시
    #첫 등장에 잡아버리기 (break)
    for y, str in enumerate(wallpaper):
        if "#" in str:
            lux = str.index("#")
            luy = y
            break      
    #end x,y 표시
    for y, str in enumerate(wallpaper):
        if "#" in str:
            rdx = str.index("#")
            rdy = y
    
    

    
    
    #정리
    answer = [lux, luy, rdx, rdy]
    return answer

    
    
    #정리
    answer = [lux, luy, rdx, rdy]
    return answer

wallpaper = [".#...", "..#..", "...#."]

solution(wallpaper=wallpaper)