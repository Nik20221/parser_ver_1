import requests
import json

loop = 1

def get_id():

    global shet_v_chetv, tot_b, tot_m
    Request_URL_0 = requests.get("https://1xstavka.ru/LiveFeed/Get1x2_VZip?sports=3&count=50&antisports=188&mode=4&country=1&partner=51&getEmpty=true").text
    json_dict_0 = json.loads(Request_URL_0)

    total_0 = json_dict_0["Value"]
    k = 1
    lis = 0
    lis_1 = 0
    for i in total_0:
        # id для следующего json
        id_match = i.get('I')
        id_match_0 = str(id_match)

        Request_URL_1 = requests.get("https://1xstavka.ru/LiveFeed/GetGameZip?id=" + id_match_0 + "&lng=en&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2").text
        print("..................NEXT MATCH......................" + '\n', sep='')
        # print("2 json: " + "https://1xstavka.ru/LiveFeed/GetGameZip?id=" + id_match_0 + "&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2")

        json_dict_1 = json.loads(Request_URL_1)
        total_0 = json_dict_1["Value"]

        # НАЗВАНИЯ КОМАНД
        print("КОМАНДЫ:")
        print(str(json_dict_1["Value"]["O1"]) + " - " + str(json_dict_1["Value"]["O2"]) + '\n', sep='')

        # ВИД МАТЧА
        print("ВИД МАТЧА: ")
        try:
            print(str(json_dict_1["Value"]["MIO"]["MaF"]) + '\n', sep='')
        except:
            print("пояснений матчу нет" + '\n', sep='')

        #СЫЛКА НА СОБЫТИЕ
        LI = i.get('LI')
        LE_0 = i.get('LE')
        LE_1 = LE_0.replace(' ', '-')
        LE_2 = LE_1.replace('.', '')
        url = str(json_dict_1["Value"]["O1"]) + "-" + str(json_dict_1["Value"]["O2"])
        url_1 = url.replace(' ', '-')
        url_2 = url_1.replace('(', '')
        url_3 = url_2.replace(')', '')

        # print("ССЫЛКА НА МАТЧ - ОБЩАЯ: ")
        # print("https://1xstavka.ru/live/Basketball/" + str(LI) + "-" + str(LE_2) + "/" + str(id_match) + "-" + url_3)

        try:
            online_ch = json_dict_1["Value"]["SG"][0]["I"]
            print("ССЫЛКА НА ЧЕТВЕРТЬ В МАТЧЕ:")
            print("https://1xstavka.ru/live/Basketball/" + str(LI) + "-" + str(LE_2) + "/" + str(online_ch) + "-" + url_3 + '\n')

            print("3 json: " + "https://1xstavka.ru/LiveFeed/GetGameZip?id=" + str(online_ch) + "&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2" + '\n', sep='')
            Request_URL_2 = requests.get("https://1xstavka.ru/LiveFeed/GetGameZip?id=" + str(online_ch) + "&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2").text
            # print("2 json: " + Request_URL_2)
            json_dict_2 = json.loads(Request_URL_2)

            # ----------------------------------------------massiv------------------------------------------
            mas = []

            # ---------------------------------------------chetvert------------------------------------------
            chetv = json_dict_2["Value"]["P"]
            print("идет " + str(chetv) + " четверть" + '\n')

            mas.append(chetv)

            # ------------------------------------------ВРЕМЯ---------------------------------------------
            print("--------TIME-------")
            time_0 = json_dict_2["Value"]["SC"]["TS"]
            print(str(time_0 // 60) + " мин: " + str(time_0 % 60) + " сек")
            time_1 = time_0 // 60

            mas.append(time_1)


            # --------------------------------- количество видов ставок ------------------------------------------
            v_st = json_dict_2["Value"]["EGC"]
            # print("КОЛИЧЕСТВО ВИДОВ СТАВОК: " + str(v_st) + '\n')

            mas.append(v_st)

            # ----------------------------------------СЧЕТ В ЧЕТВЕРТИ----------------------------------------------
            if v_st > 4:
                try:
                    if chetv == 4:
                        print("СЧЕТ В ЧЕТВЕРТИ:")
                        print(int(json_dict_2["Value"]["SC"]["PS"][3]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][3]["Value"]['S2']))
                        shet_v_chetv = int(json_dict_2["Value"]["SC"]["PS"][3]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][3]["Value"]['S2'])
                        mas.append(shet_v_chetv)
                    else:
                        if chetv == 3:
                            print("СЧЕТ В ЧЕТВЕРТИ:")
                            print(int(json_dict_2["Value"]["SC"]["PS"][2]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][2]["Value"]['S2']))
                            shet_v_chetv = int(json_dict_2["Value"]["SC"]["PS"][2]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][2]["Value"]['S2'])
                            mas.append(shet_v_chetv)
                        else:
                            if chetv == 2:
                                print("СЧЕТ В ЧЕТВЕРТИ:")
                                print(int(json_dict_2["Value"]["SC"]["PS"][1]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][1]["Value"]['S2']))
                                shet_v_chetv = int(json_dict_2["Value"]["SC"]["PS"][1]["Value"]['S1']) + int(json_dict_2["Value"]["SC"]["PS"][1]["Value"]['S2'])
                                mas.append(shet_v_chetv)
                            else:
                                if chetv == 1:
                                    print("СЧЕТ В ЧЕТВЕРТИ:")
                                    print(int(json_dict_2["Value"]["SC"]["PS"][0]["Value"]['S1']) +int(json_dict_2["Value"]["SC"]["PS"][0]["Value"]['S2']))
                                    shet_v_chetv = int(json_dict_2["Value"]["SC"]["PS"][0]["Value"]['S1']) +int(json_dict_2["Value"]["SC"]["PS"][0]["Value"]['S2'])
                                    mas.append(shet_v_chetv)
                                else:
                                    print("нихера не добавился счет в четверти - 1 ошибка в цикле")

                except:
                    print("нихера не добавился счет в четверти - 2 ошибка в цикле")
            else:
                print("количество ставок меньше 4")

            #-----------------------------------------------TOTALS--------------------------------------------
            print("TOTALS:")

            try:
                online_ch_1 = json_dict_2["Value"]["GE"][1]["E"][0]
                print("Тоталы больше:")
                for i in online_ch_1:
                    print("коэффициент: " + str(i["C"]) + " при счете: " + str(i["P"]))
                    tot_b = i["P"]
                    stavka_1 = i["C"]

                online_ch_2 = json_dict_2["Value"]["GE"][1]["E"][1]
                print("Тотал меньше:")
                for i in online_ch_2:
                    print("коэффициент: " + str(i["C"]) + " при счете: " + str(i["P"]))
                    tot_m = i["P"]
                    stavka_2 = i["C"]

                print('\n', sep='')
            except:
                print("-------- Ошибка в тоталах------или просто из нет--------")


            #----------------------------------------------ФОЛЫ -------------------------------------------------
            try:
                fols_1 = json_dict_2["Value"]["SC"]["ST"][0]["Value"][0]["S1"]
                fols_2 = json_dict_2["Value"]["SC"]["ST"][0]["Value"][0]["S2"]
                print("фолы 1 команды - " + str(fols_1) + ", фолы 2 команды - " + str(fols_2))
                print('\n', sep='')
            except:
                print("доп инфы нет" + '\n', sep='')


            #----------------------------------------ГЛАВНАЯ ФУНКЦИЯ ---------------------------------------------------
            print("--------главная функция-----")
            try:
                koef_1 = (shet_v_chetv*10)/time_1 + 10
                koef_2 = (shet_v_chetv*10)/time_1 - 10
                if tot_b > koef_1 and (time_1 > 3 and time_1 < 9):
                    lis += 1
                    print("ставим на тотал больше")
                else:
                    if tot_m < koef_2 and (time_1 > 3 and time_1 < 9):
                        lis += 1
                        print("ставим на тотал меньше")
                    else:
                        print("пропускаем ставку")
            except:
                print("по формуле ставок нет или нет входных данных")

            print("--------конец главной функции--------")

            # ---------------------------добавление в массив ---------------------------------
            # return mas

        except Exception as ex:
            print(ex)
            print("---------- Error 3 json-------")
            lis_1 += 1

        print("номер матча: " + str(k))
        k += 1
        print("количество ставок: " + str(lis))
        print("количество ошибок с json 3: " + str(lis_1))


get_id()
