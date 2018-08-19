counter = 1
s = 0
for stotke in range(3):
    s100 = stotke * 100
    for petdesetke in range(5):
        s50 = petdesetke * 50
        for dvajsetke in range(11):
            s20 = dvajsetke * 20
            for desetke in range(21):
                s10 = desetke *10
                for petke in range(41):
                    s5 = petke * 5
                    for dvojke in range(101):
                        s2 = dvojke * 2
                        if s100 + s50 + s20 + s10 + s5 + s2 <= 200:
                            counter += 1

print(counter)
