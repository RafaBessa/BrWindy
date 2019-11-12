from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
import json
from pymongo import MongoClient
from bson.json_util import dumps
from flask_jsonpify import jsonify


#Classe abstrata para construir uma query
class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractproperty
    def product(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_Loadjson(self) -> None:
        pass    

    @abstractmethod
    def produce_part_Name(self) -> None:
        pass

    @abstractmethod
    def produce_part_Ano(self) -> None:
        pass

    @abstractmethod
    def produce_part_eixoX(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_eixoY(self) -> None:
        pass


#estrutura desejada do json
{
'Nome' : [],
'Ano' : [],
'eixoX' : '',
'eixoY' : ''
}


#Classe concreta (padrao) para construir uma query
class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """

        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_Loadjson(self,data) -> None:
        print(data)
        self._product.addJson(data) 

    def produce_part_Name(self) -> None:
        self._product.addNome(self._product.json["Nome"]) 

    def produce_part_Ano(self) -> None:
        self._product.addAno(self._product.json["Ano"]) 
        

    def produce_part_eixoX(self) -> None:
        self._product.addeixoX(self._product.json["eixoX"]) 

    def produce_part_eixoY(self) -> None:
        self._product.addeixoY(self._product.json["eixoY"]) 



#classe director, para que o builder funcione em uma ordem especifica
class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_full_featured_query(self,data) -> Any:
        self.builder.produce_part_Loadjson(data)
        self.builder.produce_part_Name()
        self.builder.produce_part_Ano()
        self.builder.produce_part_eixoX()
        self.builder.produce_part_eixoY()
        return self.builder.product.ReturnQuery()





class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.Nome = ""
        self.Ano = ""
        self.eixoX = ""
        self.eixoY = ""
        self.json = {}

   # def add(self, part: Any) -> None:
    #   self.parts.append(part)


    def addJson(self, part: {}) -> None:
        self.json = part

    def addNome(self, part: "") -> None:
        self.Nome = part
    
    def addAno(self, part: "" ) -> None:
        self.Ano = part
    
    def addeixoX(self, part: "") -> None:
        self.eixoX = part

    def addeixoY(self, part: "") -> None:
        self.eixoY = part

    def ReturnQuery(self) -> Any:
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
        db=client.Brwindy
        # data = db.PostsTest.find({
        #       "Name": str(self.Nome) ,
        #       "Data.Dado.Date.Year": str(self.Ano),
        #     },
        #     {'Name':1,
        #     'Data.Dado.Date.Year':1, 
        #     ('Data.Dado.'+self.addeixoX):1,
        #      ('Data.Dado.'+self.addeixoY):1
        #      })
        # 
        print(('Data.Dado.' + str(self.eixoX)))
        self.eixoX = 'Data.Dado.' + str(self.eixoX)
        self.eixoY = 'Data.Dado.' + str(self.eixoY)
        data = db.PostsTest.find({
            "Name": str(self.Nome) ,
            "Data.Dado.Date.Year": str(self.Ano),
         },
            {
                'Name':1,
                'Data.Dado.Date.Year':1,
                self.eixoX:1,
                self.eixoY:1
            }
        )

        print(data)
        #print(dumps(data))
        
        return jsonify(dumps(data))