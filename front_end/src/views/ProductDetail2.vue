<template>
    <div class="columns row bg-light m-2 is-justify-content-space-between">
        <div class="card m-1 column is-3-desktop is-3-tablet is-12-mobile is-offset-2-mobile">
            <div class="column main-image-box">
                <img v-if="mainImage?.current_image" :src="mainImage?.current_image" class="mainImage image-with-shadow">
            </div>
            <div class="column m-3 fa-border">
                <div class="row is-justify-content-space-between"    >
                    <template v-for="productInventory in productInventories">
                        <div class="col-6 mt-2" v-for="mediaImage in productInventory.media">
                            <img    
                                :src="mediaImage?.get_image"
                                class="image product-inventory-image"
                                @mouseover="mainImage.previus_image = mainImage.current_image, mainImage.current_image=mediaImage?.get_image"
                                @mouseout="mainImage.current_image=mainImage.previus_image"
                                @click="mainImage.current_image=mediaImage?.get_image, mainImage.previus_image=mediaImage?.get_image"
                            >
                        </div>
                    </template>
                    <div class="col-6 mt-2">
                        <img    
                            :src="product?.get_thumbnail"
                            class="image product-inventory-image"
                            @mouseover="mainImage.previus_image=mainImage?.current_image, mainImage.current_image=product?.get_thumbnail"
                            @mouseout="mainImage.current_image=mainImage?.previus_image"
                            @click="mainImage.current_image=product?.get_thumbnail, mainImage.previus_image=product?.get_thumbnail"
                        >
                    </div>
                </div>
            </div>
        </div>
        <div class="column is-3-desktop is-3-tablet is-12-mobile ml-3">
            <div class="columns row is-justify-content-space-around is-flex-direction-row">
                <div v-for="attr in selectiveProductAttributes" class="box m-2 column is-5 is-10-tablet">
                    <h3>{{ attr?.name }}</h3>
                    <div v-for="value in attr.attributes" class="m-2 is-flex is-flex-directions-column is-justify-content-space-around">
                        <div class="box column is-10 is-justify-content-space-around is-flex mt-2 selected"  @click="updateSelection(attr?.name, value.attribute_value)">
                            <p>{{ value.attribute_value }}</p>
                            <img 
                                v-if="value?.attribute_value_image" :src="value?.attribute_value_image.get_image"
                                :style="`
                                        width:${value?.attribute_value_image.defualt_width}px !important;
                                        height:${value?.attribute_value_image.defualt_height}px;
                                        border-radius:${value?.attribute_value_image.default_border_radious}%;`
                                "
                                class="is-align-self-flex-esnd"
                                :class="{border: selectedProductCss.border}"
                            >

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="column is-12-mobile is-5-desktop is-5-tablet box bg-dark has-text-light">
            <div class="">
                <h3>Brand: {{ selection?.brand}}</h3>
                <template v-for="value, attr in selection?.attrs">
                    <h4>
                        Selected {{ attr }}: {{ value }}
                    </h4>
                </template>
            </div>
            <p style="text-decoration:line-through; opacity:0.5; font-size:x-small;">Price: {{ selection?.product?.store_price }}</p>
            <p>Price: {{ selection?.product?.retail_price }}</p>
            <div class="column text-center">
                <div class="button has-background-danger-50 bg-gradient column is-8 is-offset-2">
                    Add to cart <span class="icon ml-1">  <i class="fa fa-shopping-cart"></i> </span>
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
                    <span>{{attribute.attribute_values.join(" / ")}} </span>
                </span>
        </div>
    </div>
</template>

<script setup>
import axios from "axios";
import {ref, computed, onMounted} from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const product = ref(null);
const selectedProduct = ref(null);
const selection = ref({"attrs": {}})
const productInventories = ref([]);
const mainImage = ref({current_image: "", previus_image: ""});
const selectedProductCss = ref({"border": "15px solid red;", "display": "none"})

function setupSelection(productData) {
    selection.value.brand = productData?.brand?.name;
    selection.value.product = productData;
    productData.attributes.forEach((attr) => {
        if(attr.product_attribute.is_selective == true) {
            selection.value.attrs[attr.product_attribute.name] = attr.attribute_value;
    }
    })
}
function checkProductAttribute(product, attrs) {
    for (const [s_attr_name,s_attr_value]  of Object.entries(attrs)) {
            let match_case = product.attributes.find((p_attr) => p_attr.product_attribute.name == s_attr_name)
            if (match_case.attribute_value != s_attr_value) {
                return false
            }
     };
     return true
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
}

function getProduct() {
    const product_slug = route.params.product_slug
    const category_slug = route.params.category_slug
    axios
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
});

onMounted(() => {
    getProduct();
})

</script>

<style scoped>
.image-with-shadow {
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Horizontal offset, vertical offset, blur radius, color */
}
.mainImage {
    width: 100%;
    height:19rem;
    object-fit: fill;
    /* border: 5px 5px 5px 5px linear-gradient(135deg, rgba(245, 3, 3, 0), rgb(244, 70, 70)); */
    /* background-image: linear-gradient(135deg, rgba(255, 0, 0, 0), rgb(143 135 135)); */
    /* filter: drop-shadow(2px 2px 5px rgb(0 0 0 / 0.5)); */
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
    /* border: 1px solid black;
    border-radius: 0px 5px 5px 0px; */
}
.attribute-box {
    border: 1px solid black;
    border-radius: 5px;
    font-size:1.8vw;
}
</style>