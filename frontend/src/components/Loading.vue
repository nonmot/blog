<template>
    <v-container>
        <vue-loading type="bubbles" color="#242424" :size="{ width: '50px', height: '50px' }"></vue-loading>
    </v-container>
</template>

<script>
import { VueLoading } from 'vue-loading-template'

export default {
    components: {
        VueLoading
    }
}
</script>