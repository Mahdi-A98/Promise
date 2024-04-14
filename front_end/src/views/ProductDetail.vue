<template>
    <!-- <p id="mainString" class="m-3" style="break-inside: auto; word-break: break-all; letter-spacing: 0.08em; word-spacing: 0.15em;">
        {{ JSON.stringify(productInventories[0]?.attributes) }}
    </p> -->
        <div class="card m-1 column is-3 is-col-from-end">
            <div class="column main-image-box">
                <img :src="mainImage.current_image" class="mainImage">
            </div>
            <div class="column m-3 fa-border">
                <div class="row justify-content-space-between is-12 is-dark"    >
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
        <div v-for="attr in getSelectiveProductAttributes(productInventories)" class="box m-2">
            <h3>{{ attr.product_attribute?.name }}</h3>
            <div v-for="value in filterAttributeValues(getSelectiveProductAttributes(productInventories), attr)">
                {{ JSON.stringify(value)}}
            </div>
        </div>
    <div class="skeleton-block m-2 is-dark has-text-primary-00 p-2">
        <p>{{ product?.description }}</p>
    </div>
    <div class="box is-multiline">
        <template v-for="productInventory in productInventories">
            <div class="mt-2 row attribute-box" v-for="attribute in productInventory.attributes">
                <span class="col-2 attribute-name">{{ attribute.product_attribute.name }}</span>
                <span class="col-10 attribute-value">{{attribute.attribute_value}}</span>
            </div>
        </template>
    </div>
</template>

<script>
import axios from "axios"
export default {
    name : "productDetail",
    data() {
        return {
            product : null,
            productInventories: [],
            mainImage: {current_image: "", previus_image: ""}
        }
    },
    methods: {
        getProduct() {
            const product_slug = this.$route.params.product_slug
            const category_slug = this.$route.params.category_slug
            axios
                .get(`/api/inventory/${category_slug}/${product_slug}`)
                .then(response => {
                    this.productInventories = response.data
                    this.product = response.data[0].product
                    this.mainImage.current_image = this.product?.get_thumbnail
                })
                .catch(error => {
                    console.log(error)
                });
        },
        getProductAttributes(productInventories) {
            const attributeList = []
            if (productInventories?.length >= 1) {
                for (let pI in productInventories) {
                    attributeList.push(productInventories[pI]?.attributes);
                }
            }
            return attributeList.flat()
        },
        getSelectiveProductAttributes(productInventories) {
            return this.getProductAttributes(productInventories).filter((attr) => attr?.product_attribute.is_selective === true)
        },
        filterAttributeValues(attrs, attr){
            const attribute_values = []
            attrs.filter((attribute) => attribute.product_attribute.id == attr.product_attribute.id).forEach(element => {
                attribute_values.push(element);
            });
            return attribute_values
        }
    },
    mounted() {
        this.getProduct(),
        this.getProductAttributes()
    },
}
</script>
<style scoped>
.mainImage:hover {
    transform: scale3d(1.1, 1.1, 1); 
    cursor: pointer; 
    transition: transform 1s; 
}
.main-image-box {
    overflow: hidden;
    /* background-color: aqua; */
}
.product-inventory-image {
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