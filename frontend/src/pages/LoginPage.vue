<template>
    <v-container>
        <v-form
            @submit.prevent="submitLogin"
        >
            <v-text-field
                label="Eメール"
                v-model="form.email"
            ></v-text-field>
            <v-text-field
                label="パスワード"
                type="password"
                v-model="form.password"
            ></v-text-field>
            <v-btn
                type="submit"
            >ログイン</v-btn>
        </v-form>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            form: {
                email: '',
                password: ''
            }
        }
    },

    methods: {
        submitLogin() {
            this.$store.dispatch('login', {
                email: this.form.email,
                password: this.form.password
            })
            .then(() => {
                this.$router.push('/')
            })
        }
    }
}
</script>