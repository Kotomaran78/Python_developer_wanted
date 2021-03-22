import csv #обработка csv файла
import os #создание папки
import shutil #копирование фото

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader: #обработка массива по строчки
        # print(line["Image Index"],' : ',line["Finding Labels"]),
        res1 = line["Finding Labels"].split("|")# Если фото имеет несколько меток, разделяем их по "|", и получаем массив ['метка1', 'метка2'], иначе просто ['метка1']
        index_folder = '001'#номер папки с фото

        
        for val in res1:#обработка массива по метки
            # print(val)
            try:
                os.mkdir(val)#созадаем папку с названием метки
            except OSError:#если папка с таким названием уже создана, идем дальше
                pass
            
            for i in range(13):#для того чтобы пройтись по исходным папкам 1-12
                try: 
                    shutil.copy('images_'+index_folder[-3:]+'\\'+line["Image Index"], val)#копируем фото в папку с текщей меткой(val), на вход:('путь до исходной фотки','название папки куда копировать')
                except FileNotFoundError:#если файл не найден в текущей папке-исходнике, переходим к следующей
                    index_folder = '00'+str(i+1)
                else:#если файл найден, завершаем цикл
                    print(line["Image Index"],' : ',line["Finding Labels"],' : ',val,'  from:images_'+index_folder[-3:])# [-3:] - вытаскивает последние три символа из переменной
                    break


 
if __name__ == "__main__":
    with open("Data_Entry_2017.csv") as f_obj:#открываем csv как f_obj
        csv_dict_reader(f_obj) #передает в функцию файл, который открыли