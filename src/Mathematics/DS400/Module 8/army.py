unit_1_str = 20461
unit_1_loss = 6158

unit_1 = unit_1_str + unit_1_loss

unit_2_str = 20461
unit_2_loss = 6158

unit_2 = unit_2_str + unit_2_loss

unit_3_str = 20241
unit_3_loss = 7396

unit_3 = unit_3_str + unit_3_loss

cal_str = 7774
cal_loss = 345

cal = cal_str + cal_loss

total_str = 68937
total_loss = 20057

total = total_str + total_loss

# Find the probability that a randomly selected soldier was from the III Corps.
round( unit_3_str / total_str, 4 )

# Find the probability that a soldier in this army was lost in the battle.
round( total_loss / total_str, 4 )

# Find the probability that a I Corps soldier was lost in the battle.
round( unit_1_loss / unit_1_str, 4 )

# Which group had the highest probability of not being lost in the​ battle?
round( cal_loss / cal_str, 4 )

# Which group had the highest probability of​ loss?
round( unit_3_loss / unit_3_str, 4 )