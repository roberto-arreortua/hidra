from rest_framework import serializers
from .models import Config, Head
from django.utils import timezone
import json
import datetime

def coincide_año(obj, dateInit, dateEnd):
    if((obj.fecha_publicacion <= dateInit and dateInit <= obj.fecha_despublicacion)or (obj.fecha_publicacion <= dateEnd and dateEnd <= obj.fecha_despublicacion) or
        (obj.fecha_publicacion == dateInit or obj.fecha_publicacion == dateEnd or obj.fecha_despublicacion == dateInit or obj.fecha_despublicacion == dateEnd)):
        return(True)
    else:
        return(False)

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        #fields = ('active',)
        fields = '__all__'



class ConfigSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'
    
   


    def create(self,data):
        
        
        dateInit = data['fecha_publicacion']
        dateEnd = data['fecha_despublicacion']

        init = [data['lunes_inicio'],data['martes_inicio'],data['miercoles_inicio'],data['jueves_inicio'],data['viernes_inicio'],data['sabado_inicio'],data['domingo_inicio']]
        end = [data['lunes_fin'],data['martes_fin'],data['miercoles_fin'],data['jueves_fin'],data['viernes_fin'],data['sabado_fin'],data['domingo_fin']]
        days = 7
        
        #Traemos todas las configuraciones del head seleccionado 
        x = Config.objects.filter(head = data['head'])

        #los inicios y fines tiene el mismo tamaño por la condicion de que ambos deben ser None 
        lunes = x.filter(lunes_inicio__isnull = False )
        martes = x.filter(martes_inicio__isnull = False )
        miercoles = x.filter(miercoles_inicio__isnull = False )
        jueves = x.filter(jueves_inicio__isnull = False )
        viernes = x.filter(viernes_inicio__isnull = False )
        sabado = x.filter(sabado_inicio__isnull = False )
        domingo = x.filter(domingo_inicio__isnull = False )

        
       
        
        for i in range(7):
            if ((init[i] and not(end[i])) or (not(init[i]) and end[i])):
                raise serializers.ValidationError("No puede haber un inicio sin un fin ni un fin sin un inicio")
            if(init[i] and end[i]) and (init[i] == end[i]):
                raise serializers.ValidationError("Las horas de inicio y fin no pueden ser iguales ")

            
            if (init[i] and end[i]):
                if(i == 0):
                    for obj in lunes:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.lunes_inicio != None):
                            x = ((obj.lunes_inicio < init[i] and init[i] < obj.lunes_fin) or (obj.lunes_inicio < end[i] and end[i] < obj.lunes_fin) 
                            or (init[i] == obj.lunes_inicio or init[i] == obj.lunes_fin) or (end[i] == obj.lunes_inicio or end[i] == obj.lunes_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
    
                if(i == 1):
                    for obj in martes:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.martes_inicio != None):
                            x = ((obj.martes_inicio < init[i] and init[i] < obj.martes_fin) or (obj.martes_inicio < end[i] and end[i] < obj.martes_fin) 
                            or (init[i] == obj.martes_inicio or init[i] == obj.martes_fin) or (end[i] == obj.martes_inicio or end[i] == obj.martes_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
                if(i == 2):
                    for obj in miercoles:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.miercoles_inicio != None ):
                            x = ((obj.miercoles_inicio < init[i] and init[i] < obj.miercoles_fin) or (obj.miercoles_inicio < end[i] and end[i] < obj.miercoles_fin) 
                            or (init[i] == obj.miercoles_inicio or init[i] == obj.miercoles_fin) or (end[i] == obj.miercoles_inicio or end[i] == obj.miercoles_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
                if(i == 3):
                    for obj in jueves:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.jueves_inicio != None ):
                            x = ((obj.jueves_inicio < init[i] and init[i] < obj.jueves_fin) or (obj.jueves_inicio < end[i] and end[i] < obj.jueves_fin) 
                            or (init[i] == obj.jueves_inicio or init[i] == obj.jueves_fin) or (end[i] == obj.jueves_inicio or end[i] == obj.jueves_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
                if(i == 4):
                    for obj in viernes:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.viernes_inicio != None ):
                            x = ((obj.viernes_inicio < init[i] and init[i] < obj.viernes_fin) or (obj.viernes_inicio < end[i] and end[i] < obj.viernes_fin) 
                            or (init[i] == obj.viernes_inicio or init[i] == obj.viernes_fin) or (end[i] == obj.viernes_inicio or end[i] == obj.viernes_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
                if(i == 5):
                    for obj in sabado:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.sabado_inicio != None ):
                            x = ((obj.sabado_inicio < init[i] and init[i] < obj.sabado_fin) or (obj.sabado_inicio < end[i] and end[i] < obj.sabado_fin)  
                            or (init[i] == obj.sabado_inicio or init[i] == obj.sabado_fin) or (end[i] == obj.sabado_inicio or end[i] == obj.sabado_fin))
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
                if(i == 6):
                    for obj in domingo:
                        bol =  coincide_año(obj, dateInit, dateEnd)
                        if (obj.domingo_inicio != None ):
                            x = ((obj.domingo_inicio < init[i] and init[i] < obj.domingo_fin) or (obj.domingo_inicio < end[i] and end[i] < obj.domingo_fin) 
                            or (init[i] == obj.domingo_inicio or init[i] == obj.domingo_fin) or (end[i] == obj.domingo_inicio or end[i] == obj.domingo_fin))  
                            if (x and bol):
                                raise serializers.ValidationError("Esa fecha se traslapa por favor verifiquela")
            
    
        datenow = timezone.now()
        datenow = datetime.datetime(datenow.year, datenow.month, datenow.day)
        dateInit = datetime.datetime(dateInit.year, dateInit.month, dateInit.day)
        dateEnd =  datetime.datetime(dateEnd.year, dateEnd.month, dateEnd.day)

        
        if(dateInit > dateEnd or datenow > dateInit):
            raise serializers.ValidationError("fechas incorrectas ")
          
    
        else:
            config = Config(
            version=data['version'],
            fecha_publicacion = data['fecha_publicacion'],
            fecha_despublicacion =data['fecha_despublicacion'],
            priority = data['priority'],
            published = data['published'],
            lunes_inicio = data['lunes_inicio'],
            lunes_fin = data['lunes_fin'], 
            martes_inicio = data['martes_inicio'],
            martes_fin = data['martes_fin'],
            miercoles_inicio =data['miercoles_inicio'],
            miercoles_fin =data['miercoles_fin'],
            jueves_inicio =data['jueves_inicio'],
            jueves_fin =data['jueves_fin'],
            viernes_inicio =data['viernes_inicio'],
            viernes_fin =data['viernes_fin'],
            sabado_inicio =data['sabado_inicio'],
            sabado_fin =data['sabado_fin'],
            domingo_inicio =data['domingo_inicio'],
            domingo_fin =data['domingo_fin'],
            head= data['head'],
            file = data['file']
        )

            config.save()
            return config
        