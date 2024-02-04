<template>
    <div class="home">
        <ShoppingCart />
        <UserDetailsForm />
        <CheckoutPage />
    </div>
</template>

<script>
// @ is an alias to /src
import ShoppingCart from '@/components/ShoppingCart.vue';
import CheckoutPage from '@/components/CheckoutPage.vue';
import UserDetailsForm from '@/components/UserDetailsForm.vue';


export default {
    name: 'CheckoutView',
    components: {
        ShoppingCart,
        UserDetailsForm,
        CheckoutPage
    }
}
</script>
