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
import {ref, reactive} from "vue"
export default {
    name : "productDetail",
    data() {
        return {
            product : null,
            productInventories: [],
            productAttributes: [],
            mainImage: {current_image: "", previus_image: ""}
        }
    },
    mounted() {
        this.getProduct()
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
                    // alert(JSON.stringify(this.productInventories))
                    // document.getElementById("mainString").
                    
                })
                .catch(error => {
                    console.log(error)
                });
        },
    },
}
</script>
