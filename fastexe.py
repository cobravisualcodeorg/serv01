import tkinter as tk #line:1:import tkinter as tk
from tkinter import filedialog #line:2:from tkinter import filedialog
from threading import Thread #line:3:from threading import Thread
import os #line:4:import os
from PIL import Image ,ImageTk #line:5:from PIL import Image, ImageTk
from PyInstaller import __main__ as pyinstaller_main #line:6:from PyInstaller import __main__ as pyinstaller_main
import sys #line:7:import sys
class App :#line:9:class App:
    def __init__ (O0O0O0O000O00OOOO ,OOO00OO00OO000000 ):#line:10:def __init__(self, root):
        O0O0O0O000O00OOOO .root =OOO00OO00OO000000 #line:11:self.root = root
        O0O0O0O000O00OOOO .root .title ("FastExecutable")#line:12:self.root.title("FastExecutable")
        O0O0O0O000O00OOOO .result_text =tk .Text (O0O0O0O000O00OOOO .root ,wrap =tk .NONE )#line:15:self.result_text = tk.Text(self.root, wrap=tk.NONE)
        O0O0O0O000O00OOOO .result_text .pack (expand =True ,fill ='both')#line:16:self.result_text.pack(expand=True, fill='both')
        O0O0O0O000O00OOOO .file_path =""#line:18:self.file_path = ""
        O0O0O0O000O00OOOO .file_path_label =tk .Label (OOO00OO00OO000000 ,text ="")#line:19:self.file_path_label = tk.Label(root, text="")
        O0O0O0O000O00OOOO .file_path_label .pack (pady =5 )#line:20:self.file_path_label.pack(pady=5)
        O0O0O0O000O00OOOO .display_message ("SELECCIONA TU ARCHIVO .py")#line:23:self.display_message("SELECCIONA TU ARCHIVO .py")
        O0O0O0O000O00OOOO .root .after (2000 ,lambda :O0O0O0O000O00OOOO .display_message ("PRESIONA CONVERTIR EJECUTABLE Y LISTO"))#line:24:self.root.after(2000, lambda: self.display_message("PRESIONA CONVERTIR EJECUTABLE Y LISTO"))
        O0O0O0O000O00OOOO .select_button =tk .Button (OOO00OO00OO000000 ,text ="Seleccionar Archivo",command =O0O0O0O000O00OOOO .select_file )#line:27:self.select_button = tk.Button(root, text="Seleccionar Archivo", command=self.select_file)
        O0O0O0O000O00OOOO .select_button .pack (pady =20 ,side =tk .LEFT )#line:28:self.select_button.pack(pady=20, side=tk.LEFT)
        O0O0O0O000O00OOOO .convert_button =tk .Button (OOO00OO00OO000000 ,text ="Convertir a Ejecutable",state =tk .DISABLED ,command =O0O0O0O000O00OOOO .convert_to_executable )#line:31:self.convert_button = tk.Button(root, text="Convertir a Ejecutable", state=tk.DISABLED, command=self.convert_to_executable)
        O0O0O0O000O00OOOO .convert_button .pack (pady =10 ,side =tk .LEFT )#line:32:self.convert_button.pack(pady=10, side=tk.LEFT)
        O0O0O0O000O00OOOO .status_label =tk .Label (OOO00OO00OO000000 ,text ="")#line:35:self.status_label = tk.Label(root, text="")
        O0O0O0O000O00OOOO .status_label .pack (pady =10 )#line:36:self.status_label.pack(pady=10)
        O0O0O0O000O00OOOO .root .geometry ("600x500")#line:39:self.root.geometry("600x500")
        O0O0O0O000O00OOOO .root .resizable (width =False ,height =False )#line:40:self.root.resizable(width=False, height=False)
    def select_file (OO0O00O0O00000O00 ):#line:42:def select_file(self):
        OO0O00O0O00000O00 .file_path =filedialog .askopenfilename ()#line:43:self.file_path = filedialog.askopenfilename()
        if OO0O00O0O00000O00 .file_path :#line:44:if self.file_path:
            OO0O00O0O00000O00 .file_path_label .config (text =f"Archivo seleccionado: {os.path.basename(OO0O00O0O00000O00.file_path)}")#line:45:self.file_path_label.config(text=f"Archivo seleccionado: {os.path.basename(self.file_path)}")
            OO0O00O0O00000O00 .convert_button .config (state =tk .NORMAL )#line:46:self.convert_button.config(state=tk.NORMAL)
            OO0O00O0O00000O00 .status_label .config (text =f"Archivo seleccionado: {OO0O00O0O00000O00.file_path}")#line:47:self.status_label.config(text=f"Archivo seleccionado: {self.file_path}")
    def convert_to_executable (OOO0OOOOO0O0O0000 ):#line:49:def convert_to_executable(self):
        OOO0OOOOO0O0O0000 .display_message ("Comenzando proceso ")#line:50:self.display_message("Comenzando proceso ")
        OOO0OOOOO0O0O0000 .root .after (2000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Esto suele tardar unos minutos"))#line:51:self.root.after(2000, lambda: self.display_message("Esto suele tardar unos minutos"))
        OOO0OOOOO0O0O0000 .root .after (3000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Cargando Dependencias"))#line:52:self.root.after(3000, lambda: self.display_message("Cargando Dependencias"))
        OOO0OOOOO0O0O0000 .root .after (4000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Generando exe |"))#line:53:self.root.after(4000, lambda: self.display_message("Generando exe |"))
        OOO0OOOOO0O0O0000 .root .after (5000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Generando exe /"))#line:54:self.root.after(5000, lambda: self.display_message("Generando exe /"))
        OOO0OOOOO0O0O0000 .root .after (6000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Generando exe |"))#line:55:self.root.after(6000, lambda: self.display_message("Generando exe |"))
        OOO0OOOOO0O0O0000 .root .after (7000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Generando exe /"))#line:56:self.root.after(7000, lambda: self.display_message("Generando exe /"))
        OOO0OOOOO0O0O0000 .root .after (8000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias"))#line:57:self.root.after(8000, lambda: self.display_message("Verificando Librerias"))
        OOO0OOOOO0O0O0000 .root .after (10000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias."))#line:58:self.root.after(10000, lambda: self.display_message("Verificando Librerias."))
        OOO0OOOOO0O0O0000 .root .after (11000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias.."))#line:59:self.root.after(11000, lambda: self.display_message("Verificando Librerias.."))
        OOO0OOOOO0O0O0000 .root .after (12000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias..."))#line:60:self.root.after(12000, lambda: self.display_message("Verificando Librerias..."))
        OOO0OOOOO0O0O0000 .root .after (13000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias...."))#line:61:self.root.after(13000, lambda: self.display_message("Verificando Librerias...."))
        OOO0OOOOO0O0O0000 .root .after (14000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias....."))#line:62:self.root.after(14000, lambda: self.display_message("Verificando Librerias....."))
        OOO0OOOOO0O0O0000 .root .after (15000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias......."))#line:63:self.root.after(15000, lambda: self.display_message("Verificando Librerias......."))
        OOO0OOOOO0O0O0000 .root .after (16000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Verificando Librerias........."))#line:64:self.root.after(16000, lambda: self.display_message("Verificando Librerias........."))
        OOO0OOOOO0O0O0000 .root .after (17000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Validando dependencias de sistema /"))#line:65:self.root.after(17000, lambda: self.display_message("Validando dependencias de sistema /"))
        OOO0OOOOO0O0O0000 .root .after (18000 ,lambda :OOO0OOOOO0O0O0000 .display_message (" Validando dependencias de sistema |"))#line:66:self.root.after(18000, lambda: self.display_message(" Validando dependencias de sistema |"))
        OOO0OOOOO0O0O0000 .root .after (19000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Validando dependencias de sistema /"))#line:67:self.root.after(19000, lambda: self.display_message("Validando dependencias de sistema /"))
        OOO0OOOOO0O0O0000 .root .after (20000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Validando dependencias de sistema |"))#line:68:self.root.after(20000, lambda: self.display_message("Validando dependencias de sistema |"))
        OOO0OOOOO0O0O0000 .root .after (21000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Finalizando proceso de conversión."))#line:69:self.root.after(21000, lambda: self.display_message("Finalizando proceso de conversión."))
        OOO0OOOOO0O0O0000 .root .after (22000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Finalizando proceso de conversión.."))#line:70:self.root.after(22000, lambda: self.display_message("Finalizando proceso de conversión.."))
        OOO0OOOOO0O0O0000 .root .after (23000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Finalizando proceso de conversión..."))#line:71:self.root.after(23000, lambda: self.display_message("Finalizando proceso de conversión..."))
        OOO0OOOOO0O0O0000 .root .after (24000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Finalizando proceso de conversión...."))#line:72:self.root.after(24000, lambda: self.display_message("Finalizando proceso de conversión...."))
        OOO0OOOOO0O0O0000 .root .after (25000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Finalizando ajustes y optimizaciones"))#line:73:self.root.after(25000, lambda: self.display_message("Finalizando ajustes y optimizaciones"))
        OOO0OOOOO0O0O0000 .root .after (26000 ,lambda :OOO0OOOOO0O0O0000 .display_message ("Se le indicara cuando la conversión se halla realizado. "))#line:74:self.root.after(26000, lambda: self.display_message("Se le indicara cuando la conversión se halla realizado. "))
        if not OOO0OOOOO0O0O0000 .file_path :#line:79:if not self.file_path:
            OOO0OOOOO0O0O0000 .status_label .config (text ="Por favor, selecciona un archivo antes de convertir.")#line:80:self.status_label.config(text="Por favor, selecciona un archivo antes de convertir.")
            return #line:81:return
        OOO0OOOOO0O0O0000 .convert_button .config (state =tk .DISABLED )#line:84:self.convert_button.config(state=tk.DISABLED)
        OOO0000O00000OO0O =Thread (target =OOO0OOOOO0O0O0000 .run_conversion )#line:87:conversion_thread = Thread(target=self.run_conversion)
        OOO0000O00000OO0O .start ()#line:88:conversion_thread.start()
    def run_conversion (OO00OO00OO00000O0 ):#line:90:def run_conversion(self):
        try :#line:91:try:
            if not OO00OO00OO00000O0 .file_path :#line:92:if not self.file_path:
                raise ValueError ("No se ha seleccionado ningún archivo.")#line:93:raise ValueError("No se ha seleccionado ningún archivo.")
            OO00OO00OO00000O0 .convert_file_to_executable (OO00OO00OO00000O0 .file_path )#line:96:self.convert_file_to_executable(self.file_path)
        except Exception as OOOO0O00OOOOO00O0 :#line:97:except Exception as e:
            OO00OO00OO00000O0 .display_message (f"Error durante la conversión: {str(OOOO0O00OOOOO00O0)}")#line:98:self.display_message(f"Error durante la conversión: {str(e)}")
        finally :#line:99:finally:
            OO00OO00OO00000O0 .convert_button .config (state =tk .NORMAL )#line:101:self.convert_button.config(state=tk.NORMAL)
            OO00OO00OO00000O0 .root .after (1000 ,lambda :OO00OO00OO00000O0 .display_message (f"Archivo en {os.path.dirname(os.path.abspath(OO00OO00OO00000O0.file_path))}"))#line:102:self.root.after(1000, lambda: self.display_message(f"Archivo en {os.path.dirname(os.path.abspath(self.file_path))}"))
            OO00OO00OO00000O0 .root .after (2000 ,lambda :OO00OO00OO00000O0 .display_message ("Busca la carpeta Dist en la ubicacion Indicada"))#line:103:self.root.after(2000, lambda: self.display_message("Busca la carpeta Dist en la ubicacion Indicada"))
            OO00OO00OO00000O0 .root .after (3000 ,lambda :OO00OO00OO00000O0 .display_message (f"Archivo en {os.path.dirname(os.path.abspath(OO00OO00OO00000O0.file_path))}"))#line:104:self.root.after(3000, lambda: self.display_message(f"Archivo en {os.path.dirname(os.path.abspath(self.file_path))}"))
    def convert_file_to_executable (O0OO00O000OOO0OOO ,O0OO00O0OOO000O0O ):#line:105:def convert_file_to_executable(self, file_path):
        try :#line:106:try:
            OOOO00OO00O0000OO =pyinstaller_main .run (['--onefile',os .path .abspath (O0OO00O0OOO000O0O )])#line:110:])
            if OOOO00OO00O0000OO is not None :#line:112:if spec_file is not None:
                OOOO0OOOO000O0O0O =os .path .join (os .path .dirname (OOOO00OO00O0000OO ),'dist')#line:113:dist_folder = os.path.join(os.path.dirname(spec_file), 'dist')
                O0OOOOOO00O0O00O0 =os .path .join (OOOO0OOOO000O0O0O ,os .path .basename (O0OO00O0OOO000O0O ).replace ('.py','.exe'))#line:114:executable_path = os.path.join(dist_folder, os.path.basename(file_path).replace('.py', '.exe'))
                O0OO00O000OOO0OOO .display_message (f" convercion éxitosa. Su archivo Exe encuentra en la ubicación: {O0OOOOOO00O0O00O0}")#line:116:self.display_message(f" convercion éxitosa. Su archivo Exe encuentra en la ubicación: {executable_path}")
            else :#line:117:else:
                O0OO00O000OOO0OOO .display_message ("Conversión completada")#line:119:self.display_message("Conversión completada")
        except Exception as OO0O0O00O0OO000O0 :#line:122:except Exception as e:
            raise OO0O0O00O0OO000O0 #line:123:raise e
    def display_message (O0O0O0000O0OO0OO0 ,O0O000000OOO0O00O ,O0O00O00O0O0OOO0O =True ):#line:125:def display_message(self, message, clear=True):
        if O0O00O00O0O0OOO0O :#line:126:if clear:
            O0O0O0000O0OO0OO0 .result_text .delete ('1.0',tk .END )#line:127:self.result_text.delete('1.0', tk.END)  # Limpiar el contenido actual
            O0O0O0000O0OO0OO0 .root .after (1000 ,lambda :O0O0O0000O0OO0OO0 .result_text .insert (tk .END ,O0O000000OOO0O00O +"\n"))#line:130:self.root.after(1000, lambda: self.result_text.insert(tk.END, message + "\n"))
        else :#line:131:else:
            O0O0O0000O0OO0OO0 .result_text .insert (tk .END ,O0O000000OOO0O00O +"\n")#line:132:self.result_text.insert(tk.END, message + "\n")
def resource_path (O000O0OOO0OO0O00O ):#line:134:def resource_path(relative_path):
    ""#line:135:"""Get absolute path to resource, works for dev and for PyInstaller"""
    try :#line:136:try:
        OOO0O00O0O0O000OO =sys ._MEIPASS #line:138:base_path = sys._MEIPASS
    except AttributeError :#line:139:except AttributeError:
        OOO0O00O0O0O000OO =os .path .abspath (".")#line:140:base_path = os.path.abspath(".")
    return os .path .join (OOO0O00O0O0O000OO ,O000O0OOO0OO0O00O )#line:142:return os.path.join(base_path, relative_path)
if __name__ =="__main__":#line:144:if __name__ == "__main__":
    root =tk .Tk ()#line:145:root = tk.Tk()  
    image =Image .new ("RGBA",(16 ,16 ),(255 ,255 ,255 ,0 ))#line:148:image = Image.new("RGBA", (16, 16), (255, 255, 255, 0))
    tk_image =ImageTk .PhotoImage (image )#line:149:tk_image = ImageTk.PhotoImage(image)
    root .tk .call ('wm','iconphoto',root ._w ,tk_image )#line:152:root.tk.call('wm', 'iconphoto', root._w, tk_image)
    app =App (root )#line:155:app = App(root)
    root .mainloop ()#line:157:root.mainloop()
