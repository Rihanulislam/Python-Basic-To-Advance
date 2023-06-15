{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJXAZYEChB5vw4Qe/i4grK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/UniqueCoderRihan/Python-Basic-To-Advance/blob/main/variable_and_data_type_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A48pC19u0_xN",
        "outputId": "c4c37a2c-0973-403f-bc8f-e9b408ebda7c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n",
            "Your name is  Raihan sharif\n",
            "Your age is  19\n",
            "Current Year: 200\n",
            "<class 'int'>\n",
            "What is your gf name: fhsdkjf\n",
            "Type of gf name  <class 'str'>\n",
            "{'name': 'kobir', 'age': 30, 'gfs': '10'}\n",
            "{'name': 'kobir', 'age': 30}\n",
            "Name is exiting on dic kobir\n",
            "Number of Items;  2\n",
            "13\n"
          ]
        }
      ],
      "source": [
        "# Variable\n",
        "# here is example about variable;\n",
        "print('Hello World')\n",
        "name = 'Raihan sharif';\n",
        "age = 19;\n",
        "print('Your name is ',name)\n",
        "print('Your age is ',age)\n",
        "\n",
        "# type of data\n",
        "# converted string to int\n",
        "currentyear = int(input('Current Year: '))\n",
        "print(type(currentyear))\n",
        "# without converted\n",
        "gf_name = input('What is your gf name: ')\n",
        "print('Type of gf name ',type(gf_name))\n",
        "\n",
        "# dict type data\n",
        "bio ={\"name\":'kobir',\"age\":30}\n",
        "# modifey value\n",
        "bio[\"name\"]=\"kobir\"\n",
        "\n",
        "# adding value\n",
        "bio['gfs'] = '10'\n",
        "print(bio)\n",
        "\n",
        "# removeing value on dictonary\n",
        "del bio[\"gfs\"]\n",
        "print(bio)\n",
        "\n",
        "# cheking key exiting.\n",
        "if \"name\" in bio:\n",
        "  print('Name is exiting on dic', bio[\"name\"])\n",
        "\n",
        "# geting key value fairs\n",
        "print('Number of Items; ' ,len(bio))\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# list type\n",
        "roll = [12,13,2,31,232,3212,324,4234,423343]\n",
        "# find data by indexing\n",
        "print(roll[1])\n",
        "\n",
        "\n"
      ]
    }
  ]
}