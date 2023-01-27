//
//  HelloWorld.m
//  ASeaChat-frontend-iOS-OC
//
//  Created by huber wang on 2023/1/24.
//

#import "HelloWorld.h"
#import "AFNetworking.h"

@implementation HelloWorld

+(NSString *)getHelloWorld {
    NSString *URLString = @"http:192.168.2.2:8000";
    NSDictionary *parameters = @{};
    NSString *hw = nil;
    
    AFHTTPSessionManager *manager = [AFHTTPSessionManager manager];
    manager.responseSerializer = [AFHTTPResponseSerializer serializer];
    
    [manager GET:URLString parameters:parameters headers:nil progress:nil success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
        NSArray *a = [NSJSONSerialization JSONObjectWithData:responseObject options:NSJSONReadingMutableLeaves error:nil];
        NSLog(@"%@", a);
    } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
        NSLog(@"failure");
    }];
    
    return hw;
}

@end
