<template>
    <div class="columns row bg-light m-2 is-justify-content-space-between p-2 rounded-lg shadow-rose-200 shadow-sm">
        <div v-if="mainImage?.current_image" class="card m-1 column is-4-desktop is-6-tablet is-12-mobile is-offset-2-mobile h-fit">
            <div class="column main-image-box">
                <img v-if="mainImage?.current_image" :src="mainImage?.current_image" class="mainImage image-with-shadow">
            </div>
            <div class="column m-3 fa-border rounded-md">
                <div id="product-images-carousel" class="rowss flex flex-row is-justify-content-space-between h-36 overflow-scroll"  data-carousel="static" >
                    <template v-for="productInventory in productInventories">
                        <div class="col-3 col-lg-6 m-1 w-36 duration-700 ease-in-out" v-for="mediaImage in productInventory.media" data-carousel-item>
                            <img    
                                :src="mediaImage?.get_image"
                                class="image product-inventory-image h-full w-full object-cover"
                                @mouseover="mainImage.previus_image = mainImage.current_image, mainImage.current_image=mediaImage?.get_image"
                                @mouseout="mainImage.current_image=mainImage.previus_image"
                                @click="mainImage.current_image=mediaImage?.get_image, mainImage.previus_image=mediaImage?.get_image"
                            >
                        </div>
                    </template>
                    <div class="col-3 col-lg-6 m-1 w-36 duration-700 ease-in-out" data-carousel-item>
                        <img    
                            :src="product?.get_thumbnail"
                            class="image product-inventory-image h-full w-full"
                            @mouseover="mainImage.previus_image=mainImage?.current_image, mainImage.current_image=product?.get_thumbnail"
                            @mouseout="mainImage.current_image=mainImage?.previus_image"
                            @click="mainImage.current_image=product?.get_thumbnail, mainImage.previus_image=product?.get_thumbnail"
                        >
                    </div>
                    <button type="button" class="absolute  top-3/4 start-2 z-30 flex items-center justify-center  px-4 cursor-pointer group focus:outline-none" id="scroll-left" data-carousel-prev>
                        <span class="inline-flex items-center justify-center w-10 h-10 scale-75 rounded-full  bg-rose-600 opacity-40 dark:bg-gray-800/30 group-hover:bg-red-500 group-hover:opacity-100 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                            <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
                            </svg>
                            <span class="sr-only">Previous</span>
                        </span>
                    </button>
                    <button type="button" class="absolute top-3/4 end-2 z-30 flex items-center justify-center  px-4 cursor-pointer group focus:outline-none" id="scroll-right" data-carousel-next>
                        <span class="inline-flex items-center justify-center w-10 h-10 scale-75 rounded-full bg-rose-600 opacity-40 dark:bg-gray-800/30 group-hover:bg-red-500 group-hover:opacity-100 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                            <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                            </svg>
                            <span class="sr-only">Next</span>
                        </span>
                    </button>
                </div>
            </div>
        </div>
        <div v-if="selectiveProductAttributes.length < 4" class="column is-3-desktop is-4-tablet is-12-mobile align-items-center  overflow-y-scroll s-attr-box">
            <div class="columns row is-justify-contexnt-space-between is-flex-direction-row justify-center ">
                <SelectiveAttribute v-for="attr in selectiveProductAttributes" :attr="attr" :manySiblings="false" :updateSelection="updateSelection"/>
            </div>
        </div>
        <div class="column flex-row align-items-center h-75 flex py-5 is-12-mobile is-4-desktop is-12-tablet box bg-blue-100 has-text-light justsify-center">
            <div class="container bg-gradient border-gray-500 border-2  rounded h-75 py-5  flex flex-col justify-center justify-content-center lg:mt-2 lg:w-75 lg:max-w-md lg:flex-shrink-0">
                <h3 class="text-rose-600 my-5 text-4xl">Brand: {{ selection?.brand}}</h3>
                <template v-for="value, attr in selection?.attrs">
                    <div class="rounded-2xl bg-slate-100 py-5 my-2 text-censter ring-1 ring-inset ring-gray-900/5 lg:py-16">
                        <h4 class="text-slate-800 text-center text-pretty text-lg">
                            Selected {{ attr }}: {{ value }}
                        </h4>
                    </div>
                </template>
                <div class="row rounded-2xl mx-1 justify-content-center flex py-2 h-20 bg-slate-300">
                    <div class="text-center bg-zinc-100 opacity-75 rounded-2xl w-75 px-4 align-self-center">
                        <p class="text-center text-slate-500" style="text-decoration:line-through; opacity:0.5;">Price: {{ selection?.product?.store_price }}</p>
                        <p class="text-slate-800 text-xl italic font-mono">Price: {{ selection?.product?.retail_price }} $</p>
                    </div>
                </div>
                <div class="column text-center px-0">
                    <div class="button has-background-danger-50 bg-gradient column ring-2 ring-orange-900 ring-inset-2" @click="addToCart">
                        <span>Add to cart</span>
                        <span >
                            <span class="icon animate-bounce ml-1">  <i class="fa fa-shopping-cart"></i> </span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="selectiveProductAttributes.length >= 4" class=" row salign-items-center m-1 is-10">
            <div class="column is-12">
                <div class="row flex overflow-x-scrolsl is-justify-content-space-betsween is-flexs-diresction-row">
                    <SelectiveAttribute v-for="attr in selectiveProductAttributes" :attr="attr" :manySiblings="true" :updateSelection="updateSelection"/>
                </div>
            </div>
        </div>
    </div>
    <div class="skeleton-block m-2 is-dark has-text-primary-00 p-2">
        <p>{{ product?.description }}</p>
    </div>
    <div class="box is-multiline">
        <div class="mt-2 row attribute-box" v-for="attribute in productAttributes">
                <span class="col-2 attribute-name">{{ attribute.name }}</span>
                <span class="col-10 attribute-value">
                    <div class="row">
                        <template v-for="value in attribute.attribute_values">
                            <div class=" bg-zinc-100 p-2 m-1 mt-1 col-3 rounded-md border-1 border-stone-500 max-w-fit" :class="{'col-12': value.length > 60, 'col-5': value.length > 30}">
                                {{value}} 
                            </div>
                        </template>
                    </div>
                </span>
        </div>
    </div>
</template>

<script setup>
import SelectiveAttribute from "@/components/selectiveAttribute.vue";
import store from "@/store";
import axios from "axios";
import {ref, computed, onMounted} from "vue";
import { useRoute } from "vue-router";
import {toast} from 'bulma-toast'
const route = useRoute();
const product = ref(null);
const selectedProduct = ref(null);
const selection = ref({
    "attrs": {},
    "quantity": 0,
    "product": null
})
const productInventories = ref([]);
const mainImage = ref({current_image: "", previus_image: ""});

function addToCart() {
    if (isNaN(selection.quantity) || selection.quantity < 1) {
        selection.value.quantity = 1
    }
    else {
        selection.value.quantity += 1
    }
    const item = {"product":selection.value.product, "quantity":selection.value.quantity};
    store.commit('addToCart', item)
    toast({
        message :"the product was added to the cart",
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-left'
    })
}

function setupSelection(productData) {
    selection.value.brand = productData?.brand?.name;
    selection.value.product = productData;
    productData.attributes.forEach((attr) => {
        if(attr.product_attribute.is_selective == true) {
            selection.value.attrs[attr.product_attribute.name] = attr.attribute_value;
        }
    });
}

function checkProductAttribute(product, attrs) {
    for (const [s_attr_name,s_attr_value]  of Object.entries(attrs)) {
            let match_case = product.attributes.find((p_attr) => p_attr.product_attribute.name == s_attr_name)
            if (match_case.attribute_value != s_attr_value) {
                return false;
            }
    };
    return true;
};

function checkSelectedAttribute() {
    selectiveProductAttributes.value.forEach((attr) => {attr.attributes.forEach((attrValue) => {attrValue.isSelected=false;})});
    selectiveProductAttributes.value.forEach((attr) => {
        attr.attributes.forEach((attrValue) => {
            if (selection.value.attrs[attr.name] == attrValue.attribute_value) {
                attrValue.isSelected = true;
            }
        });
    });
}

function updateSelection(attr, value) {
    selection.value.attrs[attr] = value;
    let newProduct = productInventories.value.find((product) => {
            return checkProductAttribute(product, selection.value.attrs)
            }
        )
    if (!newProduct){
        let temp_attr = {};
        temp_attr[attr] = value;
        newProduct = productInventories.value.find((product) => {
                return checkProductAttribute(product, temp_attr)
                }
        )
        if(newProduct){
            setupSelection(newProduct);
        }
    }
    selection.value.product = newProduct;
    checkSelectedAttribute();
}

async function getProduct() {
    store.commit('setIsLoading', true)
    const product_slug = route.params.product_slug
    const category_slug = route.params.category_slug
    await axios
        .get(`/api/inventory/${category_slug}/${product_slug}`)
        .then(response => {
            productInventories.value = response.data;
            product.value = response.data[0].product;
            selectedProduct.value = response.data[0]
            setupSelection(response.data[0]);
            mainImage.value.current_image = product.value?.get_thumbnail;
        })
        .catch(error => {
            console.log(error)
        });
        store.commit('setIsLoading', false)
};

function cleanAttributes(attributes){
    const attributeList = [];
    for (let attribute in attributes){
        let alreadyExistAttribute = attributeList.find(
            attr => attr.name == attributes[attribute].product_attribute.name
        )
        if (alreadyExistAttribute){
            alreadyExistAttribute.attributes.push(attributes[attribute]);
            alreadyExistAttribute.attribute_values.push(attributes[attribute].attribute_value);
        }
        else {
            attributeList.push({
                name: attributes[attribute].product_attribute.name,
                attributes: [attributes[attribute]],
                attribute_values: [attributes[attribute].attribute_value]
            })
        }
    }
    return attributeList

}

const productAttributes = computed (() => {
    const attributeList = []
    if (productInventories.value?.length >= 1) {
        for (let pI in productInventories.value) {
            attributeList.push(productInventories.value[pI]?.attributes);
        }
    }
    return cleanAttributes(attributeList.flat())
});

const selectiveProductAttributes = computed (() => {
    return productAttributes.value.filter((attr) => attr.attributes[0]?.product_attribute.is_selective === true);
})

onMounted(() => {
    getProduct();
    const container = document.getElementById('product-images-carousel');
    const buttonLeft = document.getElementById('scroll-left');
    const buttonRight = document.getElementById('scroll-right');
    if (mainImage?.current_image){
        buttonLeft.addEventListener('click', () => {
            container.scrollLeft -= 200; // Adjust the scroll amount as needed
        });
    
        buttonRight.addEventListener('click', () => {
            container.scrollLeft += 200; // Adjust the scroll amount as needed
        });
    }


})
//  log ovwerflow of elements
var docWidth = document.documentElement.offsetWidth;
[].forEach.call(document.querySelectorAll('*'), function(el) {
    if (el.offsetWidth > docWidth) {
        try {
            // console.log(el);
            el.offsetWidth += 2;
            console.log(el.offsetWidth);
            
        } catch (error) {
            console.log(el);
            console.log(el.offsetWidth);
            
        }
    }
});
</script>


<style scoped>
#product-images-carousel{
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
    scroll-behavior: smooth;

}
.s-attr-box {
    border-radius: 15px;
    max-height: 540px;
    margin-top: 5px;
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
    scroll-behavior: smooth;
}

#product-images-carousel::-webkit-scrollbar{
    display: none;
}
.image-with-shadow {
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Horizontal offset, vertical offset, blur radius, color */
}
.mainImage {
    width: 100%;
    height:19rem;
    object-fit: fill;
}
.mainImage:hover {
    transform: scale3d(1.1, 1.1, 1); 
    cursor: pointer; 
    transition: transform 1s; 
}
.main-image-box {
    overflow: hidden;
}
.product-inventory-image {
    max-width: 100%;
    min-height: 100%;
    border-radius: 15px;
}
.attribute-name {
    background-color: rgb(31 49 51);
    color: rgb(255 255 255);
    align-content: center;
    /* font-size:1.8vw; */
}
.attribute-value {
    color: chocolate;
    background-color: rgb(237, 237, 237);
    align-content: center;
}
.attribute-box {
    border: 1px solid black;
    border-radius: 5px;
    font-size:1.8vw;
}

.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;

}

.lds-dual-ring::after{
    content: " ";
    display: block;
    height: 64px;
    margin: 8px;
    width: 64px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite ;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.is-loading-bar {
    height: 0;
    overflow: hidden;
    --webkit-transition: all 0.3s;
    
    &.is-loading {
        height: 80px;
    }
}
</style>