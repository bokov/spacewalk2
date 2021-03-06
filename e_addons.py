import pgzrun
import codecs
from pgzero.loaders import ImageLoader

hints_given = False

images_patch = ImageLoader('images')

egg1 = images_patch.egg1
egg2 = images_patch.egg2

# Here we read a bunch of characters from a file named 
# 'sekret.txt' and put them in a list named 'sekret'. You 
# can open that file yourself and see the all the characters 
# right there in front of you. But to get the secret 
# message(S) you'll need to know which characters to use, 
# and in what order.
sekret = list(codecs.open('sekret.txt','r','utf-8').read())
# For example, here is a long list of numbers that I'll name 'eb'
# This list selects the right letters in the right order to print 
# ASCII art of an Easter Bunny (the code is below this list)
eb = [1646, 567, 4039, 4367, 1924, 3096, 2038, 1581, 1756, 1939, 335, 2894, 3676, 3980, 1003, 1625, 2415, 1179, 2187, 2188, 1055, 4102, 406, 3399, 2443, 4126, 2991, 712, 3662, 969, 2007, 3206, 1240, 245, 766, 1387, 3801, 3233, 2057, 2241, 3695, 1046, 1378, 4006, 3568, 4454, 177, 1317, 957, 1715, 4173, 3378, 1244, 862, 3043, 1183, 2913, 4479, 645, 1917, 3741, 4443, 4495, 3760, 221, 815, 385, 2127, 2155, 414, 1895, 3685, 1958, 1086, 3611, 2044, 3086, 3283, 3116, 4196, 741, 2831, 4672, 4472, 3056, 3521, 15, 4608, 1990, 1937, 2402, 3066, 2925, 4411, 2554, 3226, 2948, 1305, 3075, 4480, 3993, 1925, 2569, 145, 1267, 1358, 4296, 4437, 2230, 3129, 3814, 1190, 3667, 2191, 4653, 3076, 852, 3837, 2296, 3956, 699, 516, 2596, 1330, 4389, 866, 3577, 3099, 1245, 932, 4504, 3519, 2260, 3294, 4189, 2912, 783, 3180, 2747, 3526, 3146, 943, 3688, 4206, 323, 369, 4613, 3339, 1705, 1763, 865, 2849, 4459, 4155, 763, 498, 4156, 4246, 1479, 4278, 2406, 4036, 3630, 315, 1945, 3318, 1383, 2024, 3427, 1575, 3064, 861, 893, 2974, 3114, 2992, 4359, 3774, 225, 2458, 1899, 496, 1504, 4626, 655, 925, 117, 3992, 4182, 2420, 668, 3183, 3098, 756, 759, 4521, 3916, 936, 3966, 1017, 2979, 3444, 2585, 3590, 1656, 3406, 4533, 3013, 1846, 3537, 2786, 3712, 4224, 1731, 4054, 2629, 623, 4462, 1522, 3865, 1837, 1546, 2738, 1239, 580, 1234, 1041, 2526, 2770, 2037, 3815, 1660, 3242, 890, 3277, 1075, 3493, 2627, 3868, 3747, 3136, 2528, 460, 2454, 3250, 2556, 3107, 731, 3018, 3707, 3566, 3194, 3447, 4614, 3151, 2059, 3796, 1883, 1612, 3286, 430, 1001, 687, 4323, 2197, 1577, 3266, 2462, 3232, 1672, 2762, 2765, 2429, 679, 2228, 1421, 4536, 2710, 490, 1180, 1312, 4434, 2968, 3248, 4204, 3476, 1786, 4345, 669, 3118, 2743, 4647, 2249, 1690, 3310, 1897, 4305, 2952, 2632, 2513, 694, 3550, 2973, 2401, 3465, 737, 3965, 1852, 435, 3843, 3085, 3306, 3647, 4188, 111, 981, 1235, 2602, 357, 3139, 639, 1739, 1803, 2996, 3716, 2811, 1295, 2906, 1772, 3437, 2669, 3785, 3633, 1380, 4270, 4288, 4249, 2567, 4186, 4119, 448, 2373, 4312, 4150, 696, 2052, 3928, 4438, 1626, 4291, 1246, 3903, 825, 413, 4316, 2436, 2105, 1915, 33, 4245, 1582, 4334, 2814, 3782, 2149, 2936, 3605, 718, 4078, 1253, 2535, 4512, 1645, 3125, 1564, 3963, 3942, 549, 4468, 3285, 287, 1397, 1228, 2496, 2892, 2826, 945, 1506, 1586, 4361, 4571, 3514, 586, 2866, 4208, 2572, 1853, 2769, 2264, 1256, 2564, 2949, 1029, 1825, 3615, 57, 265, 4446, 903, 3787, 2290, 1651, 169, 2183, 676, 961, 3160, 3428, 3482, 2959, 2651, 3977, 3112, 2649, 775, 915, 77, 869, 4486, 3910, 562, 2346, 4103, 3711, 3939, 4066, 2013, 2330, 3835, 2601, 3586, 3687, 1634, 4269, 1525, 933, 1968, 3722, 1642, 2356, 3564, 1918, 4240, 3115, 4375, 2048, 3813, 2470, 1797, 2715, 845, 1466, 3435, 4500, 4108, 3776, 2589, 4085, 2788, 3054, 2193, 3365, 3580, 3156, 1336, 2937, 2317, 3197, 2640, 1558, 2186, 4466, 686, 1477, 1095, 4607, 2361, 4197, 4043, 628, 4287, 4355, 2392, 2808, 3354, 2955, 2355, 3880, 3044, 994, 804, 4471, 3949, 2525, 973, 2171, 3574, 2047, 1677, 3681, 91, 39, 1136, 1099, 3984, 4570, 3353, 1545, 1702, 2779, 768, 3097, 2014, 1338, 4413, 2667, 4075, 3737, 2595, 3986, 1570, 2246, 1632, 143, 3841, 1661, 721, 656, 836, 2225, 3157, 2538, 339, 1102, 3661, 4502, 511, 1160, 2505, 4318, 1402, 4585, 2574, 2360, 690, 3078, 1286, 407, 4558, 1650, 4476, 4116, 2775, 2416, 550, 514, 1528, 3634, 1415, 3130, 962, 1038, 3628, 2292, 4611, 9, 2873, 2194, 1689, 3140, 2845, 4620, 203, 3126, 4404, 2284, 3207, 4215, 2185, 469, 2865, 3873, 897, 1682, 3032, 3175, 1678, 1775, 3404, 3729, 4238, 4082, 3704, 1175, 965, 2986, 3430, 4306, 616, 1992, 291, 2164, 4602, 4572, 1688, 4505, 657, 527, 2947, 4627, 1578, 2034, 4552, 466, 3007, 3498, 4542, 851, 3196, 4675, 3426, 1595, 4586, 1691, 1270, 1165, 3094, 649, 3072, 2329, 1969, 3055, 1552, 3563, 2638, 1569, 3334, 3641, 400, 4277, 1555, 3960, 3035, 4541, 297, 3474, 3825, 923, 4668, 3778, 3441, 1749, 518, 2328, 1995, 831, 3913, 1412, 2388, 3489, 2058, 3040, 3772, 1144, 3703, 1274, 2691, 595, 875, 2623, 4060, 1366, 1404, 2576, 437, 155, 3579, 4609, 4531, 2998, 345, 1991, 1829, 2374, 4635, 4222, 2942, 1398, 4368, 2635, 4431, 2547, 2853, 927, 2062, 2291, 3010, 2717, 1080, 1841, 4282, 708, 3400, 1842, 3495, 1216, 1591, 1541, 856, 411, 2440, 2911, 2772, 1985, 2439, 1365, 1211, 1535, 1521, 3298, 1350, 299, 1729, 3273, 2582, 1520, 4582, 3732, 1746, 1851, 4593, 2662, 1599, 3987, 1271, 651, 2773, 2386, 3340, 1370, 2258, 3914, 3885, 1585, 4299, 4257, 2494, 3562, 3336, 1242, 1967, 2784, 309, 4538, 1615, 545, 990, 3369, 3289, 426, 1556, 4194, 3231, 4015, 454, 4292, 730, 921, 423, 2331, 847, 873, 3714, 3588, 2471, 1716, 3639, 365, 1449, 1515, 75, 3820, 1551, 2118, 1422, 1516, 4171, 2491, 3898, 2234, 3718, 2587, 1810, 4329, 1414, 1514, 4661, 4135, 3656, 1264, 4474, 826, 4648, 3074, 2639, 1557, 2367, 3871, 528, 2419, 3596, 3279, 1518, 4101, 819, 1111, 428]
# Behold, the ASCII Easter Bunny!
print(''.join([sekret[ii] for ii in eb]))
# If you copy the above print command exactly as it is but replace
# `eb` with some other list of numbers that you created, you may 
# get a completely different message! If you chose the right
# numbers in the right order of course. Want another hint? 
# Open 'sekret.txt' in a text editor (this one will do) and 
# read what it says at the very end.

# Here I'm using a bunch of random-looking numbers to pull 
# clues out of 'sekret.txt' without them being visible in 
# the code that you're reading! You'll probably need to 
# find and look at both of these eggs in-game.
objects_patch = {
        82: [egg1, None,''.join([sekret[ii] for ii in [1204, 4526, 4372, 1508, 2077, 1143, 4069, 2734, 1804, 2146, 3664, 2914, 2827, 1761, 760, 2479, 3031, 3575, 2795, 1536, 1015, 3601, 3516, 650, 1773, 4185, 695, 1752, 2301, 531, 1357, 2697, 1011, 2877, 3174, 1396, 4488, 3979, 1470, 841, 2075, 2148, 2989, 2920, 886, 2019, 539, 1737, 2209, 1416, 3162, 585, 4428, 2181, 4535, 2445, 2628, 1870, 1334, 2325, 1989]])
	     , u"яйцо #1"],
        83: [egg2, None,''.join([sekret[ii] for ii in [1204, 4526, 4372, 1508, 2077, 1143, 4069, 2734, 1804, 2146, 3664, 2914, 2827, 1761, 760, 2479, 3031, 3575, 2795, 1536, 1015, 3601, 3516, 650, 1773, 4185, 695, 1752, 2301, 3937, 405, 4429, 844, 1728, 3973, 3565, 2151, 3536, 1159, 2483, 1640, 1067, 635, 576, 1509, 3502, 993, 2262, 960, 3325, 3570, 147, 3165, 3238, 3789, 4511, 3602, 3133, 4023, 3708, 2195, 4016, 2376, 1384, 1371, 2005, 3666, 4565, 3385, 2603, 1485, 4095, 3106, 1161, 4035, 2995]])
	     , u"яйцо #2"]
    }

props_patch = {
    82: [31, 4, 4],
    83: [5, 5, 4]
    }

map_patch = {
  5: u"Второе яйцо здесь!!!",
  21: u"На консолье тоже есть что смотреть. И в коде.",
  31: u"Первое яйцо спрятано в этой комнате!"
}

def patchfun(envir):
    global hints_given
    envir['objects'].update(objects_patch)
    envir['props'].update(props_patch)
    envir['items_player_may_stand_on'] += objects_patch 
    envir['items_player_may_carry'] += objects_patch 
    for ii in map_patch: envir['GAME_MAP'][ii][0] = map_patch[ii]

    #if not hints_given:
    print('\n','-'*37)
    print(u'\nСООБЩЕНИЯ (возможно, подсказки) ДЛЯ АНДРЮШИ:')
    # check if wall transparency implemented and give hint if not
    if 'adjust_wall_transparency' not in envir:
      print(u'\nПока нет прозрачности стен. Это затрудняет поиск первого яйца.\n')
    else:
      print(u"\nХорошо, ты уже написал функцию adjust_wall_transparency(). Она поможет тебе сегодня\n")
    # check if doors implemented and give hint if not
    if len(set(('door_in_room_26','open_door')) & set(envir)) < 2:
      print(u"\nУ тебя еще нет действующих дверей. Нужно будет пройти через двери чтобы найти второе яйцо.\n")
    else:
      print(u"\nАх, хорошо, у тебя есть функции для открытия дверей. Надеюсь, также есть все остальное нужное чтобы выйти на Марс.\n")
    # general hint/s
    print(u"\nВ самом коде тоже подсказки. Особенно в комментариях. Какие новые файлы в етой версии? Их не плохо бы просмотреть...\n")
    # hints_given = True
    
