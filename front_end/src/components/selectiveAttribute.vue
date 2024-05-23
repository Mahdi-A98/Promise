# In the name of GOD
<!-- # <div class="box m-2 column is-5 is-10-tablet bg-purple-100 focus:ring-offset-4 focus:ring-4 hover:bg-purple-200 focus:ring-purple-600" :class="{'selectedd': false}" :isSelected="true"> -->
<template>
    <div :class="{'is-3 is-tablet-5': manySiblings, 'is-5 is-10-tablet': !manySiblings}" class="box my-2 ml-1 column bg-purple-100 focus:ring-offset-4 focus:ring-4 hover:bg-purple-200 focus:ring-purple-600" :isSelected="true">
            <h3>{{ attr?.name }}</h3>
            <div v-for="value in attr.attributes" class="m-2 is-flex is-flex-directions-column is-justify-content-space-around">
                <div class="box column is-10 is-justify-content-space-around is-flex mt-2 bg-rose-100"  @click="updateSelection(attr?.name, value.attribute_value)" :class="{'border-dashed ring-purple-900 ring-2 ring-offset-2':value?.isSelected}">
                    <p>{{ value.attribute_value }}</p>
                    <img 
                        v-if="value?.attribute_value_image" :src="value?.attribute_value_image.get_image"
                        :style="`
                                width:${value?.attribute_value_image.defualt_width}px !important;
                                height:${value?.attribute_value_image.defualt_height}px;
                                border-radius:${value?.attribute_value_image.default_border_radious}%;`
                        "
                        class="is-align-self-flex-esnd"
                        
                    >

                </div>
            </div>
    </div>

</template>

<script setup>
import { onMounted, getCurrentInstance } from 'vue';
defineProps(['attr', 'updateSelection', 'manySiblings'])
</script>