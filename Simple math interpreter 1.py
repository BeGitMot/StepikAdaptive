s = input().replace(" plus ", "+").replace(" minus ", "-").replace(" multiply ", "*").replace(" divide ", "//")

exec("print(" + s + ")")