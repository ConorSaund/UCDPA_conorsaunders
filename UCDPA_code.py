{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPwnbTsDla1K3jBR7Gb3xFP"
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
      "cell_type": "code",
      "execution_count": 42,
      "metadata": {
        "id": "bacSi1GTP32h"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url = 'https://raw.githubusercontent.com/ConorSaund/UCDPA_conorsaunders/main/Sleep_Efficiency.csv'\n",
        "df = pd.read_csv(url)"
      ],
      "metadata": {
        "id": "dBlOEOM2QTTs"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 478
        },
        "id": "xHt7bhTcQWl0",
        "outputId": "e2104e57-b7dc-446a-9232-95615cc22964"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   ID  Age  Gender              Bedtime          Wakeup time  Sleep duration  \\\n",
              "0   1   65  Female  2021-03-06 01:00:00  2021-03-06 07:00:00             6.0   \n",
              "1   2   69    Male  2021-12-05 02:00:00  2021-12-05 09:00:00             7.0   \n",
              "2   3   40  Female  2021-05-25 21:30:00  2021-05-25 05:30:00             8.0   \n",
              "3   4   40  Female  2021-11-03 02:30:00  2021-11-03 08:30:00             6.0   \n",
              "4   5   57    Male  2021-03-13 01:00:00  2021-03-13 09:00:00             8.0   \n",
              "\n",
              "   Sleep efficiency  REM sleep percentage  Deep sleep percentage  \\\n",
              "0              0.88                    18                     70   \n",
              "1              0.66                    24                     28   \n",
              "2              0.89                    20                     70   \n",
              "3              0.51                    28                     25   \n",
              "4              0.76                    27                     55   \n",
              "\n",
              "   Light sleep percentage  Awakenings  Caffeine consumption  \\\n",
              "0                      10         0.0                   0.0   \n",
              "1                      53         3.0                   0.0   \n",
              "2                      10         1.0                   0.0   \n",
              "3                      52         3.0                  50.0   \n",
              "4                      18         3.0                   0.0   \n",
              "\n",
              "   Alcohol consumption Smoking status  Exercise frequency  \n",
              "0                  0.0            Yes                 3.0  \n",
              "1                  3.0            Yes                 3.0  \n",
              "2                  0.0             No                 3.0  \n",
              "3                  5.0            Yes                 1.0  \n",
              "4                  3.0             No                 3.0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a5ea4a26-863b-4f50-a525-01eb6ca99802\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Bedtime</th>\n",
              "      <th>Wakeup time</th>\n",
              "      <th>Sleep duration</th>\n",
              "      <th>Sleep efficiency</th>\n",
              "      <th>REM sleep percentage</th>\n",
              "      <th>Deep sleep percentage</th>\n",
              "      <th>Light sleep percentage</th>\n",
              "      <th>Awakenings</th>\n",
              "      <th>Caffeine consumption</th>\n",
              "      <th>Alcohol consumption</th>\n",
              "      <th>Smoking status</th>\n",
              "      <th>Exercise frequency</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>65</td>\n",
              "      <td>Female</td>\n",
              "      <td>2021-03-06 01:00:00</td>\n",
              "      <td>2021-03-06 07:00:00</td>\n",
              "      <td>6.0</td>\n",
              "      <td>0.88</td>\n",
              "      <td>18</td>\n",
              "      <td>70</td>\n",
              "      <td>10</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>69</td>\n",
              "      <td>Male</td>\n",
              "      <td>2021-12-05 02:00:00</td>\n",
              "      <td>2021-12-05 09:00:00</td>\n",
              "      <td>7.0</td>\n",
              "      <td>0.66</td>\n",
              "      <td>24</td>\n",
              "      <td>28</td>\n",
              "      <td>53</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>40</td>\n",
              "      <td>Female</td>\n",
              "      <td>2021-05-25 21:30:00</td>\n",
              "      <td>2021-05-25 05:30:00</td>\n",
              "      <td>8.0</td>\n",
              "      <td>0.89</td>\n",
              "      <td>20</td>\n",
              "      <td>70</td>\n",
              "      <td>10</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>No</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>40</td>\n",
              "      <td>Female</td>\n",
              "      <td>2021-11-03 02:30:00</td>\n",
              "      <td>2021-11-03 08:30:00</td>\n",
              "      <td>6.0</td>\n",
              "      <td>0.51</td>\n",
              "      <td>28</td>\n",
              "      <td>25</td>\n",
              "      <td>52</td>\n",
              "      <td>3.0</td>\n",
              "      <td>50.0</td>\n",
              "      <td>5.0</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>57</td>\n",
              "      <td>Male</td>\n",
              "      <td>2021-03-13 01:00:00</td>\n",
              "      <td>2021-03-13 09:00:00</td>\n",
              "      <td>8.0</td>\n",
              "      <td>0.76</td>\n",
              "      <td>27</td>\n",
              "      <td>55</td>\n",
              "      <td>18</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>No</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a5ea4a26-863b-4f50-a525-01eb6ca99802')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a5ea4a26-863b-4f50-a525-01eb6ca99802 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a5ea4a26-863b-4f50-a525-01eb6ca99802');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NirZXMOrRg7_",
        "outputId": "a5f0eec5-9208-4bb2-9be6-3b9512dabfad"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "ID                         0\n",
              "Age                        0\n",
              "Gender                     0\n",
              "Bedtime                    0\n",
              "Wakeup time                0\n",
              "Sleep duration             0\n",
              "Sleep efficiency           0\n",
              "REM sleep percentage       0\n",
              "Deep sleep percentage      0\n",
              "Light sleep percentage     0\n",
              "Awakenings                20\n",
              "Caffeine consumption      25\n",
              "Alcohol consumption       16\n",
              "Smoking status             0\n",
              "Exercise frequency         6\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Definition of REM/ Deep Sleep/ Light Sleep"
      ],
      "metadata": {
        "id": "rGl8j0caSouT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Visualisation\n",
        "1.   Population distribution\n",
        "2.   Number of smokers\n",
        "3.   Smoking and sleep relationship\n",
        "3.   Number of drinkers\n",
        "4.   Drinking and sleep relationship\n",
        "5.   Does number of wake ups affect type of sleep?\n",
        "6.   Does the time of sleep affect the type of sleep?\n",
        "\n"
      ],
      "metadata": {
        "id": "TYbvBxLoS8Mf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Count the number of non-null values under the \"Gender\" header\n",
        "gender_count = df['Gender'].count()\n",
        "\n",
        "# Show the distribution of Male and Female\n",
        "gender_distribution = df['Gender'].value_counts()\n",
        "\n",
        "print(\"Number of non-null values under 'Gender' header: \", gender_count)\n",
        "print(\"Distribution of Male and Female: \")\n",
        "print(gender_distribution)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yW3qY8zmW1LF",
        "outputId": "1f783fb2-056a-41c3-a8ce-8bd58b998f79"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of non-null values under 'Gender' header:  452\n",
            "Distribution of Male and Female: \n",
            "Male      228\n",
            "Female    224\n",
            "Name: Gender, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 1. Visualise the population distrubution with respect to Gender"
      ],
      "metadata": {
        "id": "bVHRDZPpZzcZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define the colors for the pie chart slices\n",
        "colors = ['#82c1c5', '#be545e']\n",
        "\n",
        "# Create a figure and set the background color\n",
        "fig, ax = plt.subplots()\n",
        "fig.set_facecolor('dimgray')\n",
        "\n",
        "# Create a pie chart and set the color of the label text to white\n",
        "_, _, autotexts = ax.pie(gender_distribution, labels=gender_distribution.index, colors=colors, autopct='%1.1f%%', textprops={'color': 'white'})\n",
        "\n",
        "# Set the color of the text on the pie chart to white\n",
        "for autotext in autotexts:\n",
        "    autotext.set_color('white')\n",
        "\n",
        "# Add a title and set the color to white\n",
        "ax.set_title('Gender Distribution', color='white')\n",
        "\n",
        "# Show the chart\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 264
        },
        "id": "azAW5o2eXGs6",
        "outputId": "3e19d642-32b4-45da-a0ff-29776be786b9"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 1. Visualise the population with respect to Age"
      ],
      "metadata": {
        "id": "DiLr0Ls9aEFt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the age data\n",
        "age_data = df['Age']\n",
        "\n",
        "# Create a figure with two subplots, one for the scatterplot and one for the boxplot\n",
        "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))\n",
        "\n",
        "# Create a scatterplot of age data\n",
        "ax1.scatter(range(len(age_data)), age_data)\n",
        "ax1.set_xlabel('Index')\n",
        "ax1.set_ylabel('Age')\n",
        "ax1.set_title('Age Scatterplot')\n",
        "\n",
        "# Create a boxplot of age data\n",
        "ax2.boxplot(age_data)\n",
        "ax2.set_xticklabels(['Age'])\n",
        "ax2.set_ylabel('Age')\n",
        "ax2.set_title('Age Boxplot')\n",
        "\n",
        "# Display the figure\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        },
        "id": "QCl0cfX9XIJp",
        "outputId": "fba5c67c-ca0e-4c1e-fb0b-c8476ca658a5"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x360 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2. Visualise the number of smokers"
      ],
      "metadata": {
        "id": "2--eKe5ocacB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the smoking status data\n",
        "smoking_data = df['Smoking status']\n",
        "\n",
        "# Count the number of smokers and non-smokers\n",
        "smoker_count = (smoking_data == 'Yes').sum()\n",
        "non_smoker_count = (smoking_data == 'No').sum()\n",
        "\n",
        "# Create a bar chart of smoker counts\n",
        "labels = ['Smokers', 'Non-Smokers']\n",
        "counts = [smoker_count, non_smoker_count]\n",
        "plt.bar(labels, counts)\n",
        "plt.title('Number of Smokers')\n",
        "plt.ylabel('Count')\n",
        "\n",
        "# Display the chart\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "ppyYlThQcfar",
        "outputId": "287ccf1e-fedd-4a3c-d97a-e978fca30c8d"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4vgXoJ-ncq6L"
      },
      "execution_count": 49,
      "outputs": []
    }
  ]
}