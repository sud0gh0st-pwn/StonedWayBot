<template>
    <div class="home">
        <MenuItem />
    </div>
</template>

<script>
// @ is an alias to /src
import MenuItem from '@/components/MenuItemList.vue'

export default {
    name: 'MenuView',
    components: {
        MenuItem
    }
}
</script>
