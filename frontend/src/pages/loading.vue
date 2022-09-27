<template>
    <div class="page-loader ">
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
    </div>
</template>

<script lang="ts">
export default {
    data: () => {
        return {

        }
    }
}
</script>





<style lang="scss" scoped>
$colors: #e100ff, #ff3300, #00f7ff, #2bff00;

.page-loader {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    top: 0;
    left: 0;
}

.cube {
    width: 40px;
    height: 40px;
    margin: 2px;

    @for $i from 1 through length($colors) {
        &:nth-child(#{$i}) {
            background-color: nth($colors, $i);

        }
    }

    &:first-child {
        animation: left 1s infinite;
    }

    &:last-child {
        animation: right 1s infinite .5s;
    }
}

@keyframes left {
    40% {
        transform: translateY(-60px);
    }

    50% {
        transform: translateY(0);
    }
}

@keyframes right {
    40% {
        transform: translateY(60px);
    }

    50% {
        transform: translateY(0);
    }
}
</style>