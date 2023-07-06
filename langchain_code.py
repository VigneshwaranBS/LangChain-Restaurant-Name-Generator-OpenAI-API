import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

from secret_key import openai_key
os.environ['OPENAI_API_KEY'] = openai_key

headers = {
    "authorization": st.secrets['openai_key'],
    "content-type" : "applications/json"
}




llm = OpenAI(temperature = 0.6)




def gen_rest_name_and_item(cuisine):
    prompt_temp_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restuarnt for {cuisine} food . suggest a fancy name for this"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_temp_name, output_key="restaurant_name")

    # second chain

    prompt_temp_item = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu item for {restaurant_name}. Return it as comma seprated list"
    )

    food_item_chain = LLMChain(llm=llm, prompt=prompt_temp_item, output_key="Menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'Menu_items']
    )

    res = chain({'cuisine': cuisine})

    return  res


if __name__ == "__main__":
    print(gen_rest_name_and_item("American"))


